from PIL import ImageColor, ImageDraw, ImageEnhance
from src.assets import HOLDS, ROUTES, COLOURS


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


def highlight_route(img, route):
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
            img = highlight_area(
                img, HOLDS[h], 2, outline_color=COLOURS[colour], outline_width=6
            )
    return img


def highlight_all(img):
    highlight_holds(img, HOLDS.keys())


def highlight_holds(img, holds):
    for hold in holds:
        img = highlight_area(img, HOLDS[hold], 2, outline_color="red", outline_width=6)

    return img
