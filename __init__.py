import sys
from antlr4 import *
from grammar.JavaScriptLexer import JavaScriptLexer
from grammar.JavaScriptParser import JavaScriptParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.startRule()

if __name__ == '__main__':
    main(sys.argv)