from antlr4 import *
from ANTLR.JavaScriptLexer import JavaScriptLexer
from ANTLR.JavaScriptParser import JavaScriptParser


class Logic:

    def __init__(self, file):
        self.file = file

    def get_lexer(self):
        input_stream = FileStream(self.file)
        lexer = JavaScriptLexer(input_stream)
        return lexer

    def get_tokens(self, lexer):
        result = lexer.getAllTokens()
        return result

    def get_parser(self, lexer):
        stream = CommonTokenStream(lexer)
        parser = JavaScriptParser(stream)
        return parser

    def get_tree(self, parser):
        tree = parser.program()
        return tree

    def to_string_tree(self, parser, tree):
        string = tree.toStringTree(parser.ruleNames)
        return string
