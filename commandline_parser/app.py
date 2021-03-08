import argparse

from parsers import create_parser
from operations import Adder
import colorful as cf

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    OPERATION_MAPPER = {
        'sum': Adder(args.numbers),
    }

    if not args.numbers:
        raise Exception("Numbers cannot be empty")

    elif len(args.numbers) != 3:
        raise Exception("Exacltly 3 numbers needed")

    operator = OPERATION_MAPPER[args.operation]

    result = operator.compute()
    print("Result of {cf.red}{}{cf.reset} operation is : {cf.green}{}{cf.reset}".format(args.operation, result, cf=cf))


if __name__ == '__main__':
    main()
