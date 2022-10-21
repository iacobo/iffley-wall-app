from PIL import Image, ImageColor, ImageDraw, ImageEnhance, ImageFont
from pathlib import Path
from src.assets import HOLDS, ALL_ROUTES as ROUTES, COLOURS, BASE_IMG
import itertools


def clean_file_name(name):
    """Remove special characters from file name."""
    name = name.lower()
    name = "".join(ch for ch in name if ch.isalnum())
    return name


# Image manipulation
def highlight_area(
    img, region, factor=2, outline_color=None, outline_width=6, label=False
):
    """Highlight specified rectangular region of image by `factor` with an
    optional colored  boarder drawn around its edges and return the result.
    """
    img = img.copy()  # Avoid changing original image.
    img_crop = img.crop(region)

    brightner = ImageEnhance.Brightness(img_crop)
    img_crop = brightner.enhance(factor)

    img.paste(img_crop, region)

    # Optionally draw a colored outline around the edge of the rectangular region.
    if outline_color:
        outline_color = ImageColor.getrgb(outline_color)

        draw = ImageDraw.Draw(img)  # Create a drawing context.
        left, upper, right, lower = region  # Get bounds.
        coords = [
            (left, upper),
            (right, upper),
            (right, lower),
            (left, lower),
            (left, upper),
        ]
        draw.line(coords, fill=outline_color, width=outline_width)

        if label:
            font = ImageFont.truetype("arial.ttf", 40)
            draw.text(
                ((left + right) // 2, upper),
                label,
                anchor="mt",
                font=font,
                fill="black",
                stroke_width=1,
                stroke_fill="white",
            )

    return img


def darken_out_of_bounds(img, hold_coords, factor=0.3):
    left = min([c[0] for c in hold_coords]) - 200
    right = max([c[2] for c in hold_coords]) + 200
    region_left = (0, 0, max(left, 0), img.height)
    region_right = (min(right, img.width), 0, img.width, img.height)

    img = img.copy()  # Avoid changing original image.

    for region in (region_left, region_right):
        img_crop = img.crop(region)

        brightner = ImageEnhance.Brightness(img_crop)
        img_crop = brightner.enhance(factor)

        img.paste(img_crop, region)

    return img


# Hold location tools
def get_center_x(hold):
    if not isinstance(hold, tuple):
        hold = HOLDS[hold]
    l, u, r, d = hold
    return (l + r) // 2


def estimate_subhold(hold):
    """Estimate the subhold of a hold based on its likely relative location."""
    num, let = int(hold[:-1]), hold[-1]
    l, u, r, d = HOLDS[num]
    split = (l + r) // 2
    if let == "A":
        subhold = (l, u, split, d)
    else:  # B, C, D, E
        subhold = (split, u, r, d)
    return subhold


def estimate_arete(hold, img_width=3505):
    """Estimate arete based on position of hold imn route."""
    if isinstance(hold, tuple):
        hold = hold[-1]
    if str(hold)[-1] in "ABCDE":
        hold = estimate_subhold(hold)
    else:
        hold = HOLDS[hold]
    if get_center_x(hold) < img_width // 2:
        arete = "left arete"
    else:
        arete = "right arete"
    return arete


def estimate_girder(hold):
    """Estimate girder based on position of penultimate hold."""
    if isinstance(hold, tuple):
        hold = hold[-1]
    if str(hold)[-1] in "ABCDE":
        hold = estimate_subhold(hold)
    else:
        hold = HOLDS[hold]
    if (
        get_center_x(hold)
        < (get_center_x("left girder") + get_center_x("middle girder")) // 2
    ):
        girder = "left girder"
    elif (
        get_center_x(hold)
        < (get_center_x("middle girder") + get_center_x("right girder")) // 2
    ):
        girder = "middle girder"
    else:
        girder = "right girder"
    return girder


def get_hold_coords(hold, i=None, route=None):
    # Getting correct girder
    if hold == "girder":
        hold = estimate_girder(ROUTES[route][i - 1])
    elif hold == "arete":
        hold = estimate_arete(ROUTES[route][i + 1])
    try:
        coords = HOLDS[hold]
    # Getting xA or xB etc
    except KeyError:
        coords = estimate_subhold(hold)
    return coords


# Clean up
def get_clean_holds(route):
    holds = ROUTES[route]
    n = len(ROUTES[route])
    clean_holds = []

    for i, hold in enumerate(holds):
        if isinstance(hold, tuple):
            clean_holds.extend((h, get_hold_coords(h, i, route), "stand") for h in hold)
        else:
            if i == (n - 1):
                colour = "finish"
            else:
                colour = "normal"
            clean_holds.append((hold, get_hold_coords(hold, i, route), colour))

    return clean_holds


# High level helper funcs
def highlight_route(route, img=BASE_IMG, regenerate=False, save=False, darken=True):
    # Avoid regenerating route if already cached.
    file_loc = Path(f"img/routes/{clean_file_name(route)}.png")

    if regenerate or not file_loc.is_file():
        holds = get_clean_holds(route)

        # Highlight holds
        for hold, coords, colour in holds:
            img = highlight_area(
                img,
                coords,
                outline_color=COLOURS[colour],
                label=str(hold),
            )

        # Highlight section of wall
        if darken:
            img = darken_out_of_bounds(img, [coord for _, coord, _ in holds])

        # Save img
        if save:
            img.save(file_loc)
    else:
        img = Image.open(file_loc)

    return img


def highlight_all(img=BASE_IMG, save=True):
    img = highlight_holds(HOLDS.keys(), img)
    if save:
        img.save(Path("img/examples/all.png"))
    return img


def highlight_holds(holds, img=BASE_IMG, darken=True):
    for hold in holds:
        img = highlight_area(
            img,
            HOLDS[hold],
            outline_color=COLOURS["normal"],
            label=str(hold),
        )

    if darken:
        coords = [HOLDS[hold] for hold in holds]
        img = darken_out_of_bounds(img, coords)

    return img


def cache_routes(img=BASE_IMG, regenerate=False, compress=True):
    for route in ROUTES:
        file_loc = Path(f"img/routes/{clean_file_name(route)}.png")
        if regenerate or not file_loc.is_file():
            print(f"Generating: {route}")
            curr_img = highlight_route(route, img, regenerate=True, save=True)
            if compress:
                curr_img = curr_img.resize(
                    (curr_img.width // 2, curr_img.height // 2), Image.LANCZOS
                )
                curr_img.save(file_loc, optimize=True, quality=50)
            else:
                curr_img.save(file_loc)


def list_holds():
    return list(HOLDS.keys())


def list_routes_containing(hold):
    """Return list of routes containing `hold`."""
    route_list = [
        route
        for route in ROUTES
        if hold
        in list(
            itertools.chain(
                *(i if isinstance(i, tuple) else (i,) for i in ROUTES[route])
            )
        )
    ]

    return route_list
