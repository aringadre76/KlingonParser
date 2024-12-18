import argparse
from parser import Parser

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Parse Klingon sentences and visualize the parse tree.")
    parser.add_argument('--infile', type=str, required=True, help="Path to the input file containing Klingon sentences.")
    parser.add_argument('--outfile', type=str, default="../examples/tree.json", help="Path to save the parsed tree JSON.")
    parser.add_argument('--visualize', action='store_true', help="Generate a tree diagram from the parsed JSON.")
    return parser


def run_klingon_parser(infile, outfile, visualize):
    klingon_parser = Parser()
    klingon_parser.parse_klingon_language(infile)
    if visualize:
        klingon_parser.visualize_tree(outfile, output_file="../examples/tree_diagram")


def main():
    arg_parser = setup_argparser()
    args = arg_parser.parse_args()
    run_klingon_parser(args.infile, args.outfile, args.visualize)


if __name__ == "__main__":
    main()
