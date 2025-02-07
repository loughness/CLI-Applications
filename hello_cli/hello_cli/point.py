import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--coordinates", 
                    nargs=2,
                    metavar=('X', 'Y'),
                    help="-> Take the cartesian coordinates %(metavar)s")

args = parser.parse_args()

print(args)