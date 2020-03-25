import sys
from antlr4 import *
from ANTLR.JavaScriptLexer import JavaScriptLexer
from ANTLR.JavaScriptParser import JavaScriptParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JavaScriptLexer(input_stream)
    for token in lexer.getAllTokens():
        if token.type != 107:
            print('token.text = "' + token.text + '" token.type = "' + str(token.type) + '"')
        else:
            print('token.text = "' + "\\n" + '" token.type = "' + str(token.type) + '"')
    # Create new lexer because method getAllTokens() delete all tokens
    input_stream = FileStream(argv[1])
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.program()
    print(tree.toStringTree(parser.ruleNames))


if __name__ == '__main__':
    sys.argv.append("C:/gitprojects/javascript-interpreter/code.js")
    main(sys.argv)
