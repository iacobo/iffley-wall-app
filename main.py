import argparse
from sys import flags
from PIL import Image, ImageColor, ImageDraw, ImageEnhance


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


u = [1750, 1560, 1380]
d = [1890, 1700, 1540]

HOLDS = {
    "left arete": (60, 730, 65, 1895),
    "left girder": (800, 5, 1010, 170),
    # "mid girder": (60, 730, 35, 1895),
    # "right girder": (60, 730, 35, 1895),
    1: (100, u[0], 350, d[0]),
    2: (1200, u[0], 1340, d[0]),
    3: (2000, u[0] - 75, 2150, d[0] - 100),
    4: (2350, u[0] - 50, 2550, d[0]),
    #
    12: (90, u[2], 250, d[2]),
    13: (500, u[2], 650, d[2]),
    14: (650, u[1], 920, d[1]),
    15: (830, 1200, 1130, 1330),
    "15A": (830, 1200, 965, 1330),
    "15B": (965, 1200, 1050, 1330),
    "15C": (1050, 1200, 1130, 1330),
    16: (1200, u[2], 1450, d[2] - 50),
    17: (1650, 1550, 1790, 1675),
    18: (1570, 1190, 1830, 1320),
    19: (2335, 1365, 2470, 1480),
    20: (2645, 1365, 2790, 1500),
    #
    39: (120, 850, 270, 990),
    40: (390, 900, 530, 1160),
    41: (600, 560, 740, 810),
    42: (930, 690, 1060, 945),
    43: (1200, 860, 1310, 990),
    44: (1560, 860, 1700, 990),
    "44A": (1560, 860, 1630, 990),
    "44B": (1630, 900, 1700, 990),
    45: (1945, 1030, 2075, 1150),
    46: (1990, 850, 2380, 940),
    47: (2565, 1035, 2780, 1150),
    #
    60: (280, 380, 410, 640),
    61: (800, 350, 940, 490),
    62: (1180, 230, 1320, 490),
    63: (1300, 530, 1440, 650),
    64: (1680, 530, 1815, 665),
    65: (2045, 375, 2175, 505),
    66: (2410, 700, 2550, 825),
    67: (2520, 420, 2675, 670),
    68: (2790, 590, 2915, 830),
    69: (2910, 390, 3040, 505),
    #
    93: (35, 165, 170, 300),
    94: (170, 0, 320, 140),
    95: (490, 175, 630, 310),
    96: (1450, 200, 1580, 325),
    "96A": (1450, 200, 1580, 270),
    97: (1445, 30, 1700, 170),
    98: (1755, 205, 1880, 330),
    99: (2050, 45, 2300, 185),
    100: (2390, 220, 2525, 350),
    101: (2660, 80, 2930, 180),
    # "right arete": (),
}

COLOURS = {
    "normal": "red",
    "stand": "orange",
    "finish": "blue",
}

ROUTES = {
    "The Ladder": (2, 17, 16, 18, 43, 44, 63, 64, 98),
    "Dynosaur": (2, 17, 16, 3, 18, 45, 63, 98),
    "The Bad": (2, 16, 43, 42, 44, "96A"),
    "The Jester": (2, 16, 43, 63, 96),
    "The Rocker": ((2, "15B", "44B"), 17, 64, 46, 20, 68, 69),
    "Question Time": (4, 19, 20, 47, 66, 69, 101),
}

if __name__ == "__main__":

    parser = argparse.ArgumentParser("main.py")
    parser.add_argument(
        "--route", help="A named route on Iffley Boulder Wall", type=str
    )
    parser.add_argument(
        "--holds", help="A list of holds to highlight.", type=int, nargs="+"
    )
    parser.add_argument(
        "--all", help="Highlights all holds.", action=argparse.BooleanOptionalAction
    )
    args = parser.parse_args()

    img = Image.open("img/iffley_wall.png")

    if args.all:
        img = highlight_all(img)
    elif args.route:
        img = highlight_route(img, args.route)
    elif args.holds:
        img = highlight_holds(img, args.holds)

    img.save("test.png")
    # img.show()  # Display the result.
