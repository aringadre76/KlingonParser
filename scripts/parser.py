import sys
from lark import Lark, Tree, Token
import json

class Parser:
    def __init__(self):
        self.start = "sentence"
        self.klingon_ebnf_grammar = None
        self.klingon_grammar_file = "klingon-grammar.bnf"
        self.parser = None
        
    def parse_klingon_language(self, infile: str):
        
        self._obtain_grammar()
        tree_list = {}
        with open(infile, 'r', encoding = 'utf=-8') as file:
            
            for line in file:
                self.parse_tree = self.parser.parse(line)
                tree = self.traverse_tree(self.parse_tree)
                tree_list[line] = tree
           
        outfile = "../examples/tree.json"
        with open(outfile, 'w') as out_file:
            json.dump(tree_list, out_file, indent = 4)
        print("Output printed to 'tree.json'.")



    def _obtain_grammar(self):
        with open(self.klingon_grammar_file, "r") as file:
            self.klingon_ebnf_grammar = file.read()
        self.parser = Lark(self.klingon_ebnf_grammar, start = self.start)
    
    
    def traverse_tree(self, node):
        if isinstance(node, Tree):
            return{
                "type":"non-terminal",
                "rule:":node.data,
                "children":[self.traverse_tree(child) for child in node.children]
            }
        elif isinstance(node, Token):
            return{
                "type":"terminal",
                "token": node.type,
                "value": node.value
                
            }

        
        

        