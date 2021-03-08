"""Configuration for parser."""

from typing import Dict, Any
from argparse import ArgumentParser
from datatypes import CustomNumberType
from actions import CustomAction


def create_parser() -> ArgumentParser:
    """Set up a parser for commandline.

    Returns:
        ArgumentParser: An object of this type
    """

    parser = ArgumentParser(description=__doc__)

    parser.version = '1.0'

    parser.add_argument('--op', action='store', choices=('sum',), dest='operation', help='Operation to be performed. One of +, *', default='sum')
    parser.add_argument('-i', '--input', action=CustomAction, type=CustomNumberType(), nargs='*', help='Three integer umbers are required', dest='numbers')
    parser.add_argument('-v', '--version', action='version', help='print version of the app')

    return parser 
