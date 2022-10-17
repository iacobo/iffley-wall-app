from PIL import Image, ImageColor, ImageDraw, ImageEnhance
from pathlib import Path
from src.assets import HOLDS, ROUTES, COLOURS, BASE_IMG


def highlight_area(img, region, factor, outline_color=None, outline_width=1):
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

    return img


def estimate_subhold(hold):
    """Estimate the subhold of a hold based on its position relative to the
    other holds.
    """
    num, let = int(hold[:-1]), hold[-1]
    l, u, r, d = HOLDS[num]
    split = (l + r) // 2
    if let == "A":
        subhold = (l, u, split, d)
    else:  # B, C, D, E
        subhold = (split, u, r, d)
    return subhold


def highlight_route(route, img=BASE_IMG):
    try:
        path = Path(f"img/routes/{route}.png")
        img = Image.open(path)
    except FileNotFoundError:
        n = len(ROUTES[route])
        for i, hold in enumerate(ROUTES[route]):
            if i == n - 1:
                colour = "finish"
            else:
                colour = "normal"
            if isinstance(hold, tuple):
                colour = "stand"
            else:
                hold = (hold,)
            for h in hold:
                try:
                    hold = HOLDS[h]
                except KeyError:
                    hold = estimate_subhold(h)
                img = highlight_area(
                    img, hold, 2, outline_color=COLOURS[colour], outline_width=6
                )
    return img


def highlight_all(img=BASE_IMG):
    img = highlight_holds(HOLDS.keys(), img)
    return img


def highlight_holds(holds, img=BASE_IMG):
    for hold in holds:
        img = highlight_area(
            img, HOLDS[hold], 1.75, outline_color="red", outline_width=6
        )

    return img


def cache_routes(img=BASE_IMG, regenerate=False):
    for route in ROUTES:
        file_loc = Path(f"img/routes/{route}.png")
        if regenerate or not file_loc.is_file():
            curr_img = highlight_route(route, img)
            curr_img.save(file_loc)
