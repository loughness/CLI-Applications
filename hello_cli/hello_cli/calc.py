import argparse

def add(a,b) -> float:
    return a + b

def sub(a, b) -> float:
    return a - b

def mul(a, b) -> float:
    return a * b

def div(a, b) -> float:
    return a / b

global_parser = argparse.ArgumentParser(prog="calc")
subparser = global_parser.add_subparsers(
    title="subcommands", help='arithmetic operations'
)

arg_template = {
    'dest': 'operands',
    'type': float,
    'nargs': 2,
    'metavar': 'OPERAND',
    'help': 'a numeric value',
}

add_parser = subparser.add_parser('add', help='add two numbers a and b')
add_parser.add_argument(**arg_template)
add_parser.set_defaults(func=add)

sub_parser = subparser.add_parser('sub', help='subtract two numbers a and b')
sub_parser.add_argument(**arg_template)
sub_parser.set_defaults(func=sub)

mul_parser = subparser.add_parser('mul', help='multiply two numbers a and b')
mul_parser.add_argument(**arg_template)
mul_parser.set_defaults(func=mul)

div_parser = subparser.add_parser('div', help='divide two numbers a and b')
div_parser.add_argument(**arg_template)
div_parser.set_defaults(func=div)

args = global_parser.parse_args()

print(args.func(*args.operands))