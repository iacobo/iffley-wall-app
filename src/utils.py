from PIL import Image, ImageColor, ImageDraw, ImageEnhance, ImageFont
from pathlib import Path
from src.assets import HOLDS, ROUTES, COLOURS, BASE_IMG
import itertools


def highlight_area(
    img, region, factor, outline_color=None, outline_width=1, label=False
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
            font = ImageFont.truetype("arial.ttf", 60)
            draw.text((left, upper), label, font=font)

    return img


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


def get_center_x(hold):
    if not isinstance(hold, tuple):
        hold = HOLDS[hold]
    l, u, r, d = hold
    return (l + r) // 2


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


def highlight_route(route, img=BASE_IMG, regenerate=False, save=False):
    # Avoid regenerating route if already cached.
    file_loc = Path(f"img/routes/{route}.png")

    if regenerate or not file_loc.is_file():
        n = len(ROUTES[route])

        for i, hold in enumerate(ROUTES[route]):
            # Colouring hold
            if isinstance(hold, tuple):
                colour = "stand"
            else:
                hold = (hold,)
                if i == n - 1:
                    colour = "finish"
                else:
                    colour = "normal"

            for h in hold:
                # Getting correct girder
                if h == "girder":
                    h = estimate_girder(ROUTES[route][i - 1])
                try:
                    hold = HOLDS[h]
                # Getting xA or xB etc
                except KeyError:
                    hold = estimate_subhold(h)
                # Highlight hold
                img = highlight_area(
                    img,
                    hold,
                    2,
                    outline_color=COLOURS[colour],
                    outline_width=6,
                    label=str(h),
                )
        if save:
            img.save(file_loc)
    else:
        img = Image.open(file_loc)
    return img


def highlight_all(img=BASE_IMG, save=True):
    img = highlight_holds(HOLDS.keys(), img)
    if save:
        img.save(Path("img/all.png"))
    return img


def highlight_holds(holds, img=BASE_IMG):
    for hold in holds:
        img = highlight_area(
            img,
            HOLDS[hold],
            1.75,
            outline_color="red",
            outline_width=6,
            label=str(hold),
        )

    return img


def cache_routes(img=BASE_IMG, regenerate=False):
    for route in ROUTES:
        file_loc = Path(f"img/routes/{route}.png")
        if regenerate or not file_loc.is_file():
            curr_img = highlight_route(route, img, regenerate=True, save=True)
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
