from PIL import Image

u = [1750, 1560, 1380]
d = [1890, 1700, 1540]

HOLDS = {
    "left arete": (60, 730, 65, 1895),
    "left girder": (800, 5, 1010, 170),
    "mid girder": (3450, 5, 3650, 205),
    "right girder": (6125, 5, 6300, 205),
    1: (100, u[0], 350, d[0]),
    2: (1200, u[0], 1340, d[0]),
    3: (2000, u[0] - 75, 2150, d[0] - 100),
    4: (2350, u[0] - 50, 2550, d[0]),
    5: (2880, 1710, 3010, 1830),
    6: (3380, 1710, 3525, 1830),
    7: (4270, 1710, 4405, 1830),
    8: (4655, 1710, 4790, 1830),
    9: (5125, 1710, 5365, 1830),
    10: (5745, 1710, 5865, 1830),
    11: (6675, 1710, 6820, 1830),
    12: (90, u[2], 250, d[2]),
    13: (500, u[2], 650, d[2]),
    14: (650, u[1], 920, d[1]),
    15: (830, 1200, 1130, 1330),
    "15A": (830, 1200, 965, 1330),
    "15B": (965, 1200, 1050, 1330),
    "15C": (1050, 1200, 1130, 1330),
    16: (1200, u[2], 1450, d[2] - 50),
    17: (1650, 1550, 1790, 1675),
    18: (1570, 1200, 1830, 1330),
    19: (2335, 1365, 2470, 1480),
    20: (2645, 1365, 2790, 1480),
    21: (3010, 1410, 3150, 1670),
    22: (3465, 1365, 3600, 1480),
    23: (3015, 1200, 3150, 1330),
    24: (3765, 1540, 3910, 1670),
    25: (3695, 1200, 3830, 1330),
    26: (4150, 1365, 4290, 1480),
    27: (4395, 1540, 4530, 1670),
    28: (4380, 1200, 4520, 1330),
    29: (4765, 1365, 4900, 1480),
    30: (5170, 1365, 5310, 1480),
    31: (5495, 1540, 5630, 1670),
    32: (5610, 1365, 5750, 1480),
    33: (5490, 1200, 5630, 1330),
    34: (5990, 1540, 6130, 1670),
    35: (5990, 1200, 6130, 1330),
    36: (6365, 1540, 6500, 1670),
    37: (6490, 1080, 6630, 1330),
    38: (6740, 1200, 6880, 1330),
    39: (120, 850, 270, 1000),
    40: (390, 900, 530, 1160),
    41: (600, 560, 740, 810),
    42: (930, 690, 1060, 945),
    43: (1200, 860, 1310, 1000),
    44: (1560, 860, 1700, 1000),
    "44A": (1560, 860, 1630, 1000),
    "44B": (1630, 900, 1700, 1000),
    45: (1945, 1030, 2075, 1150),
    46: (1990, 850, 2380, 940),
    47: (2565, 1035, 2780, 1150),
    48: (2910, 850, 3150, 1000),
    49: (3270, 1035, 3400, 1150),
    50: (3515, 750, 3650, 1000),
    51: (4070, 1035, 4200, 1150),
    52: (3950, 850, 4075, 1000),
    53: (4495, 1035, 4620, 1150),
    54: (4740, 890, 4870, 1150),
    55: (5110, 1035, 5240, 1150),
    56: (5305, 850, 5440, 1000),
    57: (5730, 850, 5870, 1000),
    58: (6165, 1035, 6290, 1150),
    59: (6610, 850, 6750, 1000),
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
    70: (3020, 705, 3150, 830),
    71: (3140, 550, 3270, 670),
    72: (3150, 260, 3280, 505),
    "72A": (3150, 260, 3280, 480),
    "72B": (3150, 480, 3280, 505),
    73: (3380, 550, 3510, 670),
    "73A": (3380, 550, 3450, 670),
    "73B": (3450, 550, 3510, 670),
    74: (3510, 390, 3640, 505),
    75: (3870, 550, 4130, 670),
    76: (4120, 390, 4250, 505),
    77: (4240, 705, 4370, 830),
    78: (4245, 550, 4495, 670),
    79: (4555, 705, 4680, 830),
    80: (4735, 550, 4860, 670),
    81: (5125, 390, 5380, 505),
    82: (4980, 705, 5110, 830),
    83: (5370, 550, 5500, 670),
    84: (5610, 705, 5740, 830),
    85: (5865, 420, 6010, 670),
    86: (5975, 710, 6240, 830),
    87: (6230, 550, 6360, 670),
    88: (4730, 390, 4990, 505),
    89: (6480, 705, 6610, 830),
    90: (6610, 420, 6750, 670),
    91: (6780, 705, 6910, 830),
    92: (6870, 250, 7010, 500),
    93: (35, 165, 170, 300),
    94: (170, 0, 320, 140),
    95: (490, 175, 630, 310),
    96: (1450, 200, 1580, 325),
    "96A": (1450, 200, 1580, 270),
    "96B": (1450, 270, 1580, 325),
    97: (1445, 30, 1700, 170),
    98: (1755, 205, 1880, 330),
    99: (2050, 60, 2300, 190),
    100: (2390, 220, 2525, 350),
    101: (2660, 60, 2930, 190),
    102: (2780, 225, 2905, 355),
    103: (3030, 60, 3165, 190),
    104: (3330, 60, 3475, 190),
    105: (3760, 60, 3900, 190),
    106: (3865, 225, 4010, 355),
    107: (4120, 60, 4255, 190),
    108: (4310, 225, 4455, 355),
    109: (4610, 225, 4755, 355),
    110: (4860, 60, 4995, 190),
    111: (5130, 225, 5275, 355),
    112: (5380, 60, 5515, 190),
    113: (5500, 225, 5760, 355),
    114: (5885, 50, 6130, 190),
    115: (6115, 200, 6245, 325),
    116: (6360, 200, 6495, 325),
    117: (6545, 40, 6800, 190),
    "right arete": (7006, 730, 7200, 1895),
}

COLOURS = {
    "normal": "red",
    "stand": "orange",
    "finish": "blue",
}

ROUTES = {
    # 1: First Steps
    "The Ladder": (2, 17, 16, 18, 43, 44, 63, 64, 98),
    "Ali G": ((30, 55), 81, 110),
    "Boing! Said Zebedee": ((34,), 85, 32, "112B"),
    "The Right Stuff": (9, 10, 32, 34, "58A", "85A", "113B"),
    "Dynosaur": (2, 17, 16, 3, 18, 45, 63, 98),
    "The Rocker": ((2, "15B", "44B"), 17, 64, 46, 20, 68, 69),
    # 2: Easy Classics
    "Question Time": (4, 19, 20, 47, 66, 69, 101),
    "Ice Cube": (8, 28, "29A", 54, "79A", 80, 108),
    "Twisted Sister": (("77B", 7), 80, "29B", 30, 81, 32, 85),
    "The Bad": (2, 16, 43, 42, 44, "96A"),
    "The Jester": (2, 16, 43, 63, 96),
    "No Problem": (17, 18, "64A", "97B"),
    # 3: Into the Fives
    "Sabre Dance": ((38, 11, 34, "58A"), "85A", 115),
    "Strong Like Bull": (10, 32, 85, 114),
    # 4: Classic Iffley
    "Overmantel": (7, 28, 51, 76, 107),
    "Laah!": (11, 36, 37, 89, 117),
    "C2": (11, 37, 10, 32, "84B", 81),
    "Chaos Theory": (7, 26, 51, 108, 105),
    "The Nose": (9, 30, 56, 81, 110),
    # 5: The Threshold Problems
    "Hate Mail": (11, 38, "58B", 91, 117),
    # 6: Hard Iffley
    "The Tall Man Rides a Shovelhead": (2, 16, 42, "61B", "97B"),
    "The Blair Witch Project": (6, 7, 25, 49, "73B", 105),
    "The Fallen": (8, 29, 51, 105),
}

BASE_IMG = Image.open("img/iffley_wall_big.png")
