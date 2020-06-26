from antlr4 import *
from ANTLR.JavaScriptLexer import JavaScriptLexer
from ANTLR.JavaScriptParser import JavaScriptParser


class Logic:

    def __init__(self, file):
        self.file = file

    def getLexer(self):
        input_stream = FileStream(self.file)
        lexer = JavaScriptLexer(input_stream)
        return lexer

    def getTokens(self, lexer):
        result = lexer.getAllTokens()
        return result

    def getParser(self, lexer):
        stream = CommonTokenStream(lexer)
        parser = JavaScriptParser(stream)
        return parser

    def getTree(self, parser):
        tree = parser.program()
        return tree

    def toStringTree(self, parser, tree):
        string = tree.toStringTree(parser.ruleNames)
        return string


#temp = Logic("code.js")
#print(temp.toStringTree(temp.getParser(temp.getLexer()), temp.getTree(temp.getParser(temp.getLexer()))))
