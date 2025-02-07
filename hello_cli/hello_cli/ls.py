import argparse 
import datetime
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="Directory Checker",
    description="A directory checker for use in the CLI",
    epilog="Thanks for using %(prog)s!",
    argument_default=argparse.SUPPRESS,
    allow_abbrev=True,
    )

general = parser.add_argument_group("General output")
general.add_argument("path", 
                     nargs="?", 
                     default=".",
                     help="-> Take the path to the target directory (default: %(default)s)",)

detailed = parser.add_argument_group("Detailed output")
detailed.add_argument("-l", 
                      "--long", 
                      action="store_true",
                      help="-> Display detailed directory content",)

args = parser.parse_args()

tagert_dir = Path(args.path)

if not tagert_dir.exists():
    parser.exit(1, message="\n---\nThe target directory does not exist\n---\n")

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
                "%b %d %H:%M:%S"
            )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name

for entry in tagert_dir.iterdir():
    # when we use SUPRESS in the ArgumentParser
    # we prevent non-supplied arguments from being stored 
    # in the arguments namespace.
    # This is why we do the try except below,
    # to make sure that it was passed in or not. 
    try:
        long = args.long
    except AttributeError:
        long = False
    print(build_output(entry, long=long))
