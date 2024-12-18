import argparse
import os
from parser import Parser

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type = str, required = True)
    #parser.add_argument('--outfile', type = str, required = True)
    return parser


def run_klingon_parser(infile):
    klingon_parser = Parser()
    klingon_parser.parse_klingon_language(infile)

def main():
    arg_parser = setup_argparser()
    args = arg_parser.parse_args()
    run_klingon_parser(args.infile)


if __name__ == "__main__":
    main()