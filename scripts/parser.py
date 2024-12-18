import sys
from lark import Lark, Tree, Token
import json
from graphviz import Digraph


class Parser:
    def __init__(self):
        self.start = "sentence"
        self.klingon_ebnf_grammar = None
        self.klingon_grammar_file = "klingon-grammar.bnf"
        self.parser = None

    def parse_klingon_language(self, infile: str):
        self._obtain_grammar()
        tree_list = {}
        with open(infile, 'r', encoding='utf-8') as file:
            for line in file:
                self.parse_tree = self.parser.parse(line.strip())
                tree = self.traverse_tree(self.parse_tree)
                tree_list[line.strip()] = tree

        outfile = "../examples/tree.json"
        with open(outfile, 'w') as out_file:
            json.dump(tree_list, out_file, indent=4)
        print("Output printed to 'tree.json'.")

    def _obtain_grammar(self):
        with open(self.klingon_grammar_file, "r") as file:
            self.klingon_ebnf_grammar = file.read()
        self.parser = Lark(self.klingon_ebnf_grammar, start=self.start)

    def traverse_tree(self, node):
        if isinstance(node, Tree):
            return {
                "type": "non-terminal",
                "rule:": node.data,
                "children": [self.traverse_tree(child) for child in node.children]
            }
        elif isinstance(node, Token):
            return {
                "type": "terminal",
                "token": node.type,
                "value": node.value
            }

    def visualize_tree(self, json_file, output_file="tree_diagram"):
        """
        Generates a tree diagram from the parsed JSON data.

        Args:
            json_file (str): Path to the JSON file containing the parse tree.
            output_file (str): Name of the output file (without extension).
        """
        with open(json_file, 'r') as file:
            data = json.load(file)

        dot = Digraph(comment='Parse Tree', format='png')  # Create a graphviz Digraph
        dot.attr(rankdir='TB')  # Top-to-bottom layout

        def add_nodes(node, parent_id=None, counter=[0]):
            """
            Recursively add nodes and edges to the graph.

            Args:
                node (dict): A node in the parse tree.
                parent_id (str): ID of the parent node.
                counter (list): Counter for unique node IDs.
            """
            node_id = f"node_{counter[0]}"
            counter[0] += 1

            # Add current node
            if node["type"] == "non-terminal":
                label = f'{node["rule:"]}'
            elif node["type"] == "terminal":
                label = f'{node["value"]} ({node["token"]})'
            dot.node(node_id, label)

            # Connect to parent
            if parent_id:
                dot.edge(parent_id, node_id)

            # Process children if they exist
            if "children" in node:
                for child in node["children"]:
                    add_nodes(child, node_id)

        # Generate the tree for each sentence
        for sentence, tree in data.items():
            root_id = f"root_{hash(sentence) % 10000}"  # Unique root node for each sentence
            dot.node(root_id, f"'{sentence.strip()}'", shape="box")
            add_nodes(tree, root_id)

        # Save and render the diagram
        output_path = dot.render(filename=output_file, cleanup=True)
        print(f"Tree diagram saved as: {output_path}")
