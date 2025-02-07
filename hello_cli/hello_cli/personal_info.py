import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-names", nargs=argparse.REMAINDER)
parser.add_argument("-dob", action="store")

args = parser.parse_args()

print(args)

# An example using the REMAINDER attribute 