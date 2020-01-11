# arg_demo2.py

import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-x', '--execute' ,action="store", required=True,
                        help='Help text for option X')
    # optional arguments
    parser.add_argument('-y', help='Help text for option Y', default=False)
    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())

    # To prevent more than one argument from running use mutually exclusive group
    group = parser._mutually_exclusive_groups()
    group.add_argument('-s', '--sum', action="store", help="help option for -s")
    

if __name__ == '__main__':
    get_args()