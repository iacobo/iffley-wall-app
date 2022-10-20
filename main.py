import argparse
from src import utils

if __name__ == "__main__":

    parser = argparse.ArgumentParser("main.py")
    parser.add_argument("--route", help="Named route on Iffley Wall", type=str)
    parser.add_argument(
        "--holds", help="List of holds to highlight.", type=int, nargs="+"
    )
    parser.add_argument(
        "--all", help="Highlight all holds.", action=argparse.BooleanOptionalAction
    )
    parser.add_argument(
        "--cache", help="Cache routes.", action=argparse.BooleanOptionalAction
    )
    parser.add_argument("--containing", help="List routes containing hold", type=int)
    args = parser.parse_args()

    if args.all:
        img = utils.highlight_all()
    elif args.route:
        img = utils.highlight_route(args.route, regenerate=True, save=True)
    elif args.holds:
        img = utils.highlight_holds(args.holds)
        # img.save("img/my_route.png")
    elif args.containing:
        routes = utils.list_routes_containing(args.containing)
        print(*routes, sep="\n")

    # Display the result.
    if args.all or args.route or args.holds:
        img.show()

    if args.cache:
        utils.cache_routes(regenerate=True)
