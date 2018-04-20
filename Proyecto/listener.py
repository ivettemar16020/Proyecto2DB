# Generated from .\sql.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sqlParser import sqlParser
else:
    from sqlParser import sqlParser

# This class defines a complete listener for a parse tree produced by sqlParser.
class sqlListener(ParseTreeListener):
	  # Enter a parse tree produced by sqlParser#create_database_stmt.
    def enterCreate_database_stmt(self, ctx:sqlParser.Create_database_stmtContext):
        pass
