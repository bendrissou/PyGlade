# Generated from tiny.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tinyParser import tinyParser
else:
    from tinyParser import tinyParser

# This class defines a complete listener for a parse tree produced by tinyParser.
class tinyListener(ParseTreeListener):

    # Enter a parse tree produced by tinyParser#program.
    def enterProgram(self, ctx:tinyParser.ProgramContext):
        pass

    # Exit a parse tree produced by tinyParser#program.
    def exitProgram(self, ctx:tinyParser.ProgramContext):
        pass


    # Enter a parse tree produced by tinyParser#stmt_list.
    def enterStmt_list(self, ctx:tinyParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by tinyParser#stmt_list.
    def exitStmt_list(self, ctx:tinyParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by tinyParser#stmt.
    def enterStmt(self, ctx:tinyParser.StmtContext):
        pass

    # Exit a parse tree produced by tinyParser#stmt.
    def exitStmt(self, ctx:tinyParser.StmtContext):
        pass


    # Enter a parse tree produced by tinyParser#assign_stmt.
    def enterAssign_stmt(self, ctx:tinyParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by tinyParser#assign_stmt.
    def exitAssign_stmt(self, ctx:tinyParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by tinyParser#read_stmt.
    def enterRead_stmt(self, ctx:tinyParser.Read_stmtContext):
        pass

    # Exit a parse tree produced by tinyParser#read_stmt.
    def exitRead_stmt(self, ctx:tinyParser.Read_stmtContext):
        pass


    # Enter a parse tree produced by tinyParser#write_stmt.
    def enterWrite_stmt(self, ctx:tinyParser.Write_stmtContext):
        pass

    # Exit a parse tree produced by tinyParser#write_stmt.
    def exitWrite_stmt(self, ctx:tinyParser.Write_stmtContext):
        pass


    # Enter a parse tree produced by tinyParser#id_list.
    def enterId_list(self, ctx:tinyParser.Id_listContext):
        pass

    # Exit a parse tree produced by tinyParser#id_list.
    def exitId_list(self, ctx:tinyParser.Id_listContext):
        pass


    # Enter a parse tree produced by tinyParser#expr_list.
    def enterExpr_list(self, ctx:tinyParser.Expr_listContext):
        pass

    # Exit a parse tree produced by tinyParser#expr_list.
    def exitExpr_list(self, ctx:tinyParser.Expr_listContext):
        pass


    # Enter a parse tree produced by tinyParser#expr.
    def enterExpr(self, ctx:tinyParser.ExprContext):
        pass

    # Exit a parse tree produced by tinyParser#expr.
    def exitExpr(self, ctx:tinyParser.ExprContext):
        pass


    # Enter a parse tree produced by tinyParser#factor.
    def enterFactor(self, ctx:tinyParser.FactorContext):
        pass

    # Exit a parse tree produced by tinyParser#factor.
    def exitFactor(self, ctx:tinyParser.FactorContext):
        pass


    # Enter a parse tree produced by tinyParser#integer.
    def enterInteger(self, ctx:tinyParser.IntegerContext):
        pass

    # Exit a parse tree produced by tinyParser#integer.
    def exitInteger(self, ctx:tinyParser.IntegerContext):
        pass


    # Enter a parse tree produced by tinyParser#op.
    def enterOp(self, ctx:tinyParser.OpContext):
        pass

    # Exit a parse tree produced by tinyParser#op.
    def exitOp(self, ctx:tinyParser.OpContext):
        pass


    # Enter a parse tree produced by tinyParser#ident.
    def enterIdent(self, ctx:tinyParser.IdentContext):
        pass

    # Exit a parse tree produced by tinyParser#ident.
    def exitIdent(self, ctx:tinyParser.IdentContext):
        pass



del tinyParser