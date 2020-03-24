import sys
from antlr4 import *
from ANTLR.JavaScriptLexer import JavaScriptLexer
from ANTLR.JavaScriptParser import JavaScriptParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.startRule()
    print(tree)


if __name__ == '__main__':
    main(sys.argv)