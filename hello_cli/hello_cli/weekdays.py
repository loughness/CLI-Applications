import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--weekday", type=int, choices=range(1,8))

args = parser.parse_args()

print(args)