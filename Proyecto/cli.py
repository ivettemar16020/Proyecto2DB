import sys
from antlr4 import *
from compiler.sqlLexer import sqlLexer
from compiler.sqlParser import sqlParser
from antlr4.error.ErrorListener import ErrorListener
from CYDBMSListener import CYDBMSListener
from DatabaseManager import DatabaseManager

# userpath = 'databases/'
# db = ''

class ParserException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ParserExceptionErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParserException("line " + str(line) + ":" + str(column) + " " + msg)

def parse(text):
    lexer = sqlLexer(InputStream(text))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ParserExceptionErrorListener())

    stream = CommonTokenStream(lexer)

    parser = sqlParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ParserExceptionErrorListener())

    # Este es el nombre de la produccion inicial de la gramatica definida en sql.g4
    tree = parser.parse()

    listener = CYDBMSListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

'''
Uso: python cli.py

Las construcciones validas para esta gramatica son todas aquellas 
'''
def main(argv):
    print("Bienvenido al DBMS de Ivette, Cristopher y Cristian: CYDBMS")
    while True:
        try:
            text = input("> ")

            if (text == 'exit'):
                sys.exit()

            parse(text);
            print("Valid")

        except ParserException as e:
            print("Got a parser exception:", e.value)

        except EOFError as e:
            print("Bye")
            sys.exit()

        except Exception as e:
            print("Got exception: ", e)

if __name__ == '__main__':
    main(sys.argv)
