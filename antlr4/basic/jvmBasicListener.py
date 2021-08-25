# Generated from jvmBasic.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jvmBasicParser import jvmBasicParser
else:
    from jvmBasicParser import jvmBasicParser

# This class defines a complete listener for a parse tree produced by jvmBasicParser.
class jvmBasicListener(ParseTreeListener):

    # Enter a parse tree produced by jvmBasicParser#prog.
    def enterProg(self, ctx:jvmBasicParser.ProgContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#prog.
    def exitProg(self, ctx:jvmBasicParser.ProgContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#line.
    def enterLine(self, ctx:jvmBasicParser.LineContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#line.
    def exitLine(self, ctx:jvmBasicParser.LineContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#amperoper.
    def enterAmperoper(self, ctx:jvmBasicParser.AmperoperContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#amperoper.
    def exitAmperoper(self, ctx:jvmBasicParser.AmperoperContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#linenumber.
    def enterLinenumber(self, ctx:jvmBasicParser.LinenumberContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#linenumber.
    def exitLinenumber(self, ctx:jvmBasicParser.LinenumberContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#amprstmt.
    def enterAmprstmt(self, ctx:jvmBasicParser.AmprstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#amprstmt.
    def exitAmprstmt(self, ctx:jvmBasicParser.AmprstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#statement.
    def enterStatement(self, ctx:jvmBasicParser.StatementContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#statement.
    def exitStatement(self, ctx:jvmBasicParser.StatementContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#vardecl.
    def enterVardecl(self, ctx:jvmBasicParser.VardeclContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#vardecl.
    def exitVardecl(self, ctx:jvmBasicParser.VardeclContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#printstmt1.
    def enterPrintstmt1(self, ctx:jvmBasicParser.Printstmt1Context):
        pass

    # Exit a parse tree produced by jvmBasicParser#printstmt1.
    def exitPrintstmt1(self, ctx:jvmBasicParser.Printstmt1Context):
        pass


    # Enter a parse tree produced by jvmBasicParser#printlist.
    def enterPrintlist(self, ctx:jvmBasicParser.PrintlistContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#printlist.
    def exitPrintlist(self, ctx:jvmBasicParser.PrintlistContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#getstmt.
    def enterGetstmt(self, ctx:jvmBasicParser.GetstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#getstmt.
    def exitGetstmt(self, ctx:jvmBasicParser.GetstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#letstmt.
    def enterLetstmt(self, ctx:jvmBasicParser.LetstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#letstmt.
    def exitLetstmt(self, ctx:jvmBasicParser.LetstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#variableassignment.
    def enterVariableassignment(self, ctx:jvmBasicParser.VariableassignmentContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#variableassignment.
    def exitVariableassignment(self, ctx:jvmBasicParser.VariableassignmentContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#relop.
    def enterRelop(self, ctx:jvmBasicParser.RelopContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#relop.
    def exitRelop(self, ctx:jvmBasicParser.RelopContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#neq.
    def enterNeq(self, ctx:jvmBasicParser.NeqContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#neq.
    def exitNeq(self, ctx:jvmBasicParser.NeqContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#ifstmt.
    def enterIfstmt(self, ctx:jvmBasicParser.IfstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#ifstmt.
    def exitIfstmt(self, ctx:jvmBasicParser.IfstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#forstmt1.
    def enterForstmt1(self, ctx:jvmBasicParser.Forstmt1Context):
        pass

    # Exit a parse tree produced by jvmBasicParser#forstmt1.
    def exitForstmt1(self, ctx:jvmBasicParser.Forstmt1Context):
        pass


    # Enter a parse tree produced by jvmBasicParser#forstmt2.
    def enterForstmt2(self, ctx:jvmBasicParser.Forstmt2Context):
        pass

    # Exit a parse tree produced by jvmBasicParser#forstmt2.
    def exitForstmt2(self, ctx:jvmBasicParser.Forstmt2Context):
        pass


    # Enter a parse tree produced by jvmBasicParser#nextstmt.
    def enterNextstmt(self, ctx:jvmBasicParser.NextstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#nextstmt.
    def exitNextstmt(self, ctx:jvmBasicParser.NextstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#inputstmt.
    def enterInputstmt(self, ctx:jvmBasicParser.InputstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#inputstmt.
    def exitInputstmt(self, ctx:jvmBasicParser.InputstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#readstmt.
    def enterReadstmt(self, ctx:jvmBasicParser.ReadstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#readstmt.
    def exitReadstmt(self, ctx:jvmBasicParser.ReadstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#dimstmt.
    def enterDimstmt(self, ctx:jvmBasicParser.DimstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#dimstmt.
    def exitDimstmt(self, ctx:jvmBasicParser.DimstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#gotostmt.
    def enterGotostmt(self, ctx:jvmBasicParser.GotostmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#gotostmt.
    def exitGotostmt(self, ctx:jvmBasicParser.GotostmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#gosubstmt.
    def enterGosubstmt(self, ctx:jvmBasicParser.GosubstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#gosubstmt.
    def exitGosubstmt(self, ctx:jvmBasicParser.GosubstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#pokestmt.
    def enterPokestmt(self, ctx:jvmBasicParser.PokestmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#pokestmt.
    def exitPokestmt(self, ctx:jvmBasicParser.PokestmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#callstmt.
    def enterCallstmt(self, ctx:jvmBasicParser.CallstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#callstmt.
    def exitCallstmt(self, ctx:jvmBasicParser.CallstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#hplotstmt.
    def enterHplotstmt(self, ctx:jvmBasicParser.HplotstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#hplotstmt.
    def exitHplotstmt(self, ctx:jvmBasicParser.HplotstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#vplotstmt.
    def enterVplotstmt(self, ctx:jvmBasicParser.VplotstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#vplotstmt.
    def exitVplotstmt(self, ctx:jvmBasicParser.VplotstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#plotstmt.
    def enterPlotstmt(self, ctx:jvmBasicParser.PlotstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#plotstmt.
    def exitPlotstmt(self, ctx:jvmBasicParser.PlotstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#ongotostmt.
    def enterOngotostmt(self, ctx:jvmBasicParser.OngotostmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#ongotostmt.
    def exitOngotostmt(self, ctx:jvmBasicParser.OngotostmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#ongosubstmt.
    def enterOngosubstmt(self, ctx:jvmBasicParser.OngosubstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#ongosubstmt.
    def exitOngosubstmt(self, ctx:jvmBasicParser.OngosubstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#vtabstmnt.
    def enterVtabstmnt(self, ctx:jvmBasicParser.VtabstmntContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#vtabstmnt.
    def exitVtabstmnt(self, ctx:jvmBasicParser.VtabstmntContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#htabstmnt.
    def enterHtabstmnt(self, ctx:jvmBasicParser.HtabstmntContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#htabstmnt.
    def exitHtabstmnt(self, ctx:jvmBasicParser.HtabstmntContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#himemstmt.
    def enterHimemstmt(self, ctx:jvmBasicParser.HimemstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#himemstmt.
    def exitHimemstmt(self, ctx:jvmBasicParser.HimemstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#lomemstmt.
    def enterLomemstmt(self, ctx:jvmBasicParser.LomemstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#lomemstmt.
    def exitLomemstmt(self, ctx:jvmBasicParser.LomemstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#datastmt.
    def enterDatastmt(self, ctx:jvmBasicParser.DatastmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#datastmt.
    def exitDatastmt(self, ctx:jvmBasicParser.DatastmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#datum.
    def enterDatum(self, ctx:jvmBasicParser.DatumContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#datum.
    def exitDatum(self, ctx:jvmBasicParser.DatumContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#waitstmt.
    def enterWaitstmt(self, ctx:jvmBasicParser.WaitstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#waitstmt.
    def exitWaitstmt(self, ctx:jvmBasicParser.WaitstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#xdrawstmt.
    def enterXdrawstmt(self, ctx:jvmBasicParser.XdrawstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#xdrawstmt.
    def exitXdrawstmt(self, ctx:jvmBasicParser.XdrawstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#drawstmt.
    def enterDrawstmt(self, ctx:jvmBasicParser.DrawstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#drawstmt.
    def exitDrawstmt(self, ctx:jvmBasicParser.DrawstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#defstmt.
    def enterDefstmt(self, ctx:jvmBasicParser.DefstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#defstmt.
    def exitDefstmt(self, ctx:jvmBasicParser.DefstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#tabstmt.
    def enterTabstmt(self, ctx:jvmBasicParser.TabstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#tabstmt.
    def exitTabstmt(self, ctx:jvmBasicParser.TabstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#speedstmt.
    def enterSpeedstmt(self, ctx:jvmBasicParser.SpeedstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#speedstmt.
    def exitSpeedstmt(self, ctx:jvmBasicParser.SpeedstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#rotstmt.
    def enterRotstmt(self, ctx:jvmBasicParser.RotstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#rotstmt.
    def exitRotstmt(self, ctx:jvmBasicParser.RotstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#scalestmt.
    def enterScalestmt(self, ctx:jvmBasicParser.ScalestmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#scalestmt.
    def exitScalestmt(self, ctx:jvmBasicParser.ScalestmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#colorstmt.
    def enterColorstmt(self, ctx:jvmBasicParser.ColorstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#colorstmt.
    def exitColorstmt(self, ctx:jvmBasicParser.ColorstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#hcolorstmt.
    def enterHcolorstmt(self, ctx:jvmBasicParser.HcolorstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#hcolorstmt.
    def exitHcolorstmt(self, ctx:jvmBasicParser.HcolorstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#hlinstmt.
    def enterHlinstmt(self, ctx:jvmBasicParser.HlinstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#hlinstmt.
    def exitHlinstmt(self, ctx:jvmBasicParser.HlinstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#vlinstmt.
    def enterVlinstmt(self, ctx:jvmBasicParser.VlinstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#vlinstmt.
    def exitVlinstmt(self, ctx:jvmBasicParser.VlinstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#onerrstmt.
    def enterOnerrstmt(self, ctx:jvmBasicParser.OnerrstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#onerrstmt.
    def exitOnerrstmt(self, ctx:jvmBasicParser.OnerrstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#prstmt.
    def enterPrstmt(self, ctx:jvmBasicParser.PrstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#prstmt.
    def exitPrstmt(self, ctx:jvmBasicParser.PrstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#instmt.
    def enterInstmt(self, ctx:jvmBasicParser.InstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#instmt.
    def exitInstmt(self, ctx:jvmBasicParser.InstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#storestmt.
    def enterStorestmt(self, ctx:jvmBasicParser.StorestmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#storestmt.
    def exitStorestmt(self, ctx:jvmBasicParser.StorestmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#recallstmt.
    def enterRecallstmt(self, ctx:jvmBasicParser.RecallstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#recallstmt.
    def exitRecallstmt(self, ctx:jvmBasicParser.RecallstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#liststmt.
    def enterListstmt(self, ctx:jvmBasicParser.ListstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#liststmt.
    def exitListstmt(self, ctx:jvmBasicParser.ListstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#popstmt.
    def enterPopstmt(self, ctx:jvmBasicParser.PopstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#popstmt.
    def exitPopstmt(self, ctx:jvmBasicParser.PopstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#amptstmt.
    def enterAmptstmt(self, ctx:jvmBasicParser.AmptstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#amptstmt.
    def exitAmptstmt(self, ctx:jvmBasicParser.AmptstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#includestmt.
    def enterIncludestmt(self, ctx:jvmBasicParser.IncludestmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#includestmt.
    def exitIncludestmt(self, ctx:jvmBasicParser.IncludestmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#endstmt.
    def enterEndstmt(self, ctx:jvmBasicParser.EndstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#endstmt.
    def exitEndstmt(self, ctx:jvmBasicParser.EndstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#returnstmt.
    def enterReturnstmt(self, ctx:jvmBasicParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#returnstmt.
    def exitReturnstmt(self, ctx:jvmBasicParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#restorestmt.
    def enterRestorestmt(self, ctx:jvmBasicParser.RestorestmtContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#restorestmt.
    def exitRestorestmt(self, ctx:jvmBasicParser.RestorestmtContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#number.
    def enterNumber(self, ctx:jvmBasicParser.NumberContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#number.
    def exitNumber(self, ctx:jvmBasicParser.NumberContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#func_.
    def enterFunc_(self, ctx:jvmBasicParser.Func_Context):
        pass

    # Exit a parse tree produced by jvmBasicParser#func_.
    def exitFunc_(self, ctx:jvmBasicParser.Func_Context):
        pass


    # Enter a parse tree produced by jvmBasicParser#signExpression.
    def enterSignExpression(self, ctx:jvmBasicParser.SignExpressionContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#signExpression.
    def exitSignExpression(self, ctx:jvmBasicParser.SignExpressionContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#exponentExpression.
    def enterExponentExpression(self, ctx:jvmBasicParser.ExponentExpressionContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#exponentExpression.
    def exitExponentExpression(self, ctx:jvmBasicParser.ExponentExpressionContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:jvmBasicParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:jvmBasicParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#addingExpression.
    def enterAddingExpression(self, ctx:jvmBasicParser.AddingExpressionContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#addingExpression.
    def exitAddingExpression(self, ctx:jvmBasicParser.AddingExpressionContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#relationalExpression.
    def enterRelationalExpression(self, ctx:jvmBasicParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#relationalExpression.
    def exitRelationalExpression(self, ctx:jvmBasicParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#expression.
    def enterExpression(self, ctx:jvmBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#expression.
    def exitExpression(self, ctx:jvmBasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#var_.
    def enterVar_(self, ctx:jvmBasicParser.Var_Context):
        pass

    # Exit a parse tree produced by jvmBasicParser#var_.
    def exitVar_(self, ctx:jvmBasicParser.Var_Context):
        pass


    # Enter a parse tree produced by jvmBasicParser#varname.
    def enterVarname(self, ctx:jvmBasicParser.VarnameContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#varname.
    def exitVarname(self, ctx:jvmBasicParser.VarnameContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#varsuffix.
    def enterVarsuffix(self, ctx:jvmBasicParser.VarsuffixContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#varsuffix.
    def exitVarsuffix(self, ctx:jvmBasicParser.VarsuffixContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#varlist.
    def enterVarlist(self, ctx:jvmBasicParser.VarlistContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#varlist.
    def exitVarlist(self, ctx:jvmBasicParser.VarlistContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#exprlist.
    def enterExprlist(self, ctx:jvmBasicParser.ExprlistContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#exprlist.
    def exitExprlist(self, ctx:jvmBasicParser.ExprlistContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#sqrfunc.
    def enterSqrfunc(self, ctx:jvmBasicParser.SqrfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#sqrfunc.
    def exitSqrfunc(self, ctx:jvmBasicParser.SqrfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#chrfunc.
    def enterChrfunc(self, ctx:jvmBasicParser.ChrfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#chrfunc.
    def exitChrfunc(self, ctx:jvmBasicParser.ChrfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#lenfunc.
    def enterLenfunc(self, ctx:jvmBasicParser.LenfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#lenfunc.
    def exitLenfunc(self, ctx:jvmBasicParser.LenfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#ascfunc.
    def enterAscfunc(self, ctx:jvmBasicParser.AscfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#ascfunc.
    def exitAscfunc(self, ctx:jvmBasicParser.AscfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#midfunc.
    def enterMidfunc(self, ctx:jvmBasicParser.MidfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#midfunc.
    def exitMidfunc(self, ctx:jvmBasicParser.MidfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#pdlfunc.
    def enterPdlfunc(self, ctx:jvmBasicParser.PdlfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#pdlfunc.
    def exitPdlfunc(self, ctx:jvmBasicParser.PdlfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#peekfunc.
    def enterPeekfunc(self, ctx:jvmBasicParser.PeekfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#peekfunc.
    def exitPeekfunc(self, ctx:jvmBasicParser.PeekfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#intfunc.
    def enterIntfunc(self, ctx:jvmBasicParser.IntfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#intfunc.
    def exitIntfunc(self, ctx:jvmBasicParser.IntfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#spcfunc.
    def enterSpcfunc(self, ctx:jvmBasicParser.SpcfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#spcfunc.
    def exitSpcfunc(self, ctx:jvmBasicParser.SpcfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#frefunc.
    def enterFrefunc(self, ctx:jvmBasicParser.FrefuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#frefunc.
    def exitFrefunc(self, ctx:jvmBasicParser.FrefuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#posfunc.
    def enterPosfunc(self, ctx:jvmBasicParser.PosfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#posfunc.
    def exitPosfunc(self, ctx:jvmBasicParser.PosfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#usrfunc.
    def enterUsrfunc(self, ctx:jvmBasicParser.UsrfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#usrfunc.
    def exitUsrfunc(self, ctx:jvmBasicParser.UsrfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#leftfunc.
    def enterLeftfunc(self, ctx:jvmBasicParser.LeftfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#leftfunc.
    def exitLeftfunc(self, ctx:jvmBasicParser.LeftfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#rightfunc.
    def enterRightfunc(self, ctx:jvmBasicParser.RightfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#rightfunc.
    def exitRightfunc(self, ctx:jvmBasicParser.RightfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#strfunc.
    def enterStrfunc(self, ctx:jvmBasicParser.StrfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#strfunc.
    def exitStrfunc(self, ctx:jvmBasicParser.StrfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#fnfunc.
    def enterFnfunc(self, ctx:jvmBasicParser.FnfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#fnfunc.
    def exitFnfunc(self, ctx:jvmBasicParser.FnfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#valfunc.
    def enterValfunc(self, ctx:jvmBasicParser.ValfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#valfunc.
    def exitValfunc(self, ctx:jvmBasicParser.ValfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#scrnfunc.
    def enterScrnfunc(self, ctx:jvmBasicParser.ScrnfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#scrnfunc.
    def exitScrnfunc(self, ctx:jvmBasicParser.ScrnfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#sinfunc.
    def enterSinfunc(self, ctx:jvmBasicParser.SinfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#sinfunc.
    def exitSinfunc(self, ctx:jvmBasicParser.SinfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#cosfunc.
    def enterCosfunc(self, ctx:jvmBasicParser.CosfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#cosfunc.
    def exitCosfunc(self, ctx:jvmBasicParser.CosfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#tanfunc.
    def enterTanfunc(self, ctx:jvmBasicParser.TanfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#tanfunc.
    def exitTanfunc(self, ctx:jvmBasicParser.TanfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#atnfunc.
    def enterAtnfunc(self, ctx:jvmBasicParser.AtnfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#atnfunc.
    def exitAtnfunc(self, ctx:jvmBasicParser.AtnfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#rndfunc.
    def enterRndfunc(self, ctx:jvmBasicParser.RndfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#rndfunc.
    def exitRndfunc(self, ctx:jvmBasicParser.RndfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#sgnfunc.
    def enterSgnfunc(self, ctx:jvmBasicParser.SgnfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#sgnfunc.
    def exitSgnfunc(self, ctx:jvmBasicParser.SgnfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#expfunc.
    def enterExpfunc(self, ctx:jvmBasicParser.ExpfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#expfunc.
    def exitExpfunc(self, ctx:jvmBasicParser.ExpfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#logfunc.
    def enterLogfunc(self, ctx:jvmBasicParser.LogfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#logfunc.
    def exitLogfunc(self, ctx:jvmBasicParser.LogfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#absfunc.
    def enterAbsfunc(self, ctx:jvmBasicParser.AbsfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#absfunc.
    def exitAbsfunc(self, ctx:jvmBasicParser.AbsfuncContext):
        pass


    # Enter a parse tree produced by jvmBasicParser#tabfunc.
    def enterTabfunc(self, ctx:jvmBasicParser.TabfuncContext):
        pass

    # Exit a parse tree produced by jvmBasicParser#tabfunc.
    def exitTabfunc(self, ctx:jvmBasicParser.TabfuncContext):
        pass



del jvmBasicParser