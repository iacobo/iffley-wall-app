import argparse
from PIL import Image
from src import utils

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
        img = utils.highlight_all(img)
    elif args.route:
        img = utils.highlight_route(img, args.route)
    elif args.holds:
        img = utils.highlight_holds(img, args.holds)

    img.save("img/output.png")
    # img.show()  # Display the result.
