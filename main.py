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


u = [1750, 1560, 1380]
d = [1890, 1700, 1540]

holds = {
    "left arete": (60, 730, 65, 1895),
    "left girder": (800, 5, 1010, 170),
    # "mid girder": (60, 730, 35, 1895),
    # "right girder": (60, 730, 35, 1895),
    1: (100, u[0], 350, d[0]),
    2: (1200, u[0], 1340, d[0]),
    3: (2000, u[0] - 75, 2150, d[0] - 100),
    4: (2350, u[0] - 50, 2550, d[0]),
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
    20: (2645, 1365, 2790, 1500),
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
    60: (280, 380, 410, 640),
    61: (800, 350, 940, 490),
    62: (1180, 230, 1320, 490),
    63: (1300, 530, 1440, 650),
    64: (1680, 530, 1815, 665),
    65: (2045, 375, 2175, 505),
    68: (2790, 590, 2915, 830),
    69: (2910, 390, 3040, 505),
    96: (1450, 200, 1580, 325),
    "96A": (1450, 200, 1580, 270),
    93: (35, 165, 170, 300),
    94: (170, 0, 320, 140),
    95: (490, 175, 630, 310),
    97: (1445, 30, 1700, 170),
    98: (1755, 205, 1880, 330),
    99: (2050, 45, 2300, 185),
    # "right arete": (),
}

colours = {
    "normal": "red",
    "stand": "orange",
    "finish": "blue",
}

routes = {
    "The Ladder": (2, 17, 16, 18, 43, 44, 63, 64, 98),
    "Dynosaur": (2, 17, 16, 3, 18, 45, 63, 98),
    "The Bad": (2, 16, 43, 42, 44, "96A"),
    "The Jester": (2, 16, 43, 63, 96),
    "The Rocker": ((2, "15B", "44B"), 17, 64, 46, 20, 68, 69),
}

if __name__ == "__main__":

    img = Image.open("img/iffley_wall.png")

    all_holds = True
    route = "The Rocker"

    if all_holds:
        for i, hold in holds.items():
            img = highlight_area(img, hold, 2, outline_color="red", outline_width=6)

    else:
        n = len(routes[route])
        for i, hold in enumerate(routes[route]):
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
                    img, holds[h], 2, outline_color=colours[colour], outline_width=6
                )

    img.save("test.png")
    # img.show()  # Display the result.
