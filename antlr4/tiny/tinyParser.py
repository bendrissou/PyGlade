# Generated from tiny.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3&\n\3\f\3\16")
        buf.write("\3)\13\3\3\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b@\n\b\f\b")
        buf.write("\16\bC\13\b\3\t\3\t\3\t\3\t\3\t\3\t\7\tK\n\t\f\t\16\t")
        buf.write("N\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nW\n\n\f\n\16\nZ")
        buf.write("\13\n\3\13\3\13\5\13^\n\13\3\f\5\fa\n\f\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\16\2\6\4\16\20\22\17\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\2\3\3\2\t\n\2c\2\34\3\2\2\2\4 \3\2\2\2")
        buf.write("\6-\3\2\2\2\b/\3\2\2\2\n\63\3\2\2\2\f\66\3\2\2\2\169\3")
        buf.write("\2\2\2\20D\3\2\2\2\22O\3\2\2\2\24]\3\2\2\2\26`\3\2\2\2")
        buf.write("\30d\3\2\2\2\32f\3\2\2\2\34\35\7\3\2\2\35\36\5\4\3\2\36")
        buf.write("\37\7\4\2\2\37\3\3\2\2\2 !\b\3\1\2!\"\5\6\4\2\"\'\3\2")
        buf.write("\2\2#$\f\4\2\2$&\5\6\4\2%#\3\2\2\2&)\3\2\2\2\'%\3\2\2")
        buf.write("\2\'(\3\2\2\2(\5\3\2\2\2)\'\3\2\2\2*.\5\b\5\2+.\5\n\6")
        buf.write("\2,.\5\f\7\2-*\3\2\2\2-+\3\2\2\2-,\3\2\2\2.\7\3\2\2\2")
        buf.write("/\60\5\32\16\2\60\61\7\5\2\2\61\62\5\22\n\2\62\t\3\2\2")
        buf.write("\2\63\64\7\6\2\2\64\65\5\16\b\2\65\13\3\2\2\2\66\67\7")
        buf.write("\7\2\2\678\5\20\t\28\r\3\2\2\29:\b\b\1\2:;\5\32\16\2;")
        buf.write("A\3\2\2\2<=\f\4\2\2=>\7\b\2\2>@\5\32\16\2?<\3\2\2\2@C")
        buf.write("\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\17\3\2\2\2CA\3\2\2\2DE\b")
        buf.write("\t\1\2EF\5\22\n\2FL\3\2\2\2GH\f\4\2\2HI\7\b\2\2IK\5\22")
        buf.write("\n\2JG\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\21\3\2\2")
        buf.write("\2NL\3\2\2\2OP\b\n\1\2PQ\5\24\13\2QX\3\2\2\2RS\f\4\2\2")
        buf.write("ST\5\30\r\2TU\5\24\13\2UW\3\2\2\2VR\3\2\2\2WZ\3\2\2\2")
        buf.write("XV\3\2\2\2XY\3\2\2\2Y\23\3\2\2\2ZX\3\2\2\2[^\5\32\16\2")
        buf.write("\\^\5\26\f\2][\3\2\2\2]\\\3\2\2\2^\25\3\2\2\2_a\7\t\2")
        buf.write("\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7\f\2\2c\27\3\2\2\2")
        buf.write("de\t\2\2\2e\31\3\2\2\2fg\7\13\2\2g\33\3\2\2\2\t\'-ALX")
        buf.write("]`")
        return buf.getvalue()


class tinyParser ( Parser ):

    grammarFileName = "tiny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'BEGIN'", "'END'", "':='", "'READ'", 
                     "'WRITE'", "','", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_stmt_list = 1
    RULE_stmt = 2
    RULE_assign_stmt = 3
    RULE_read_stmt = 4
    RULE_write_stmt = 5
    RULE_id_list = 6
    RULE_expr_list = 7
    RULE_expr = 8
    RULE_factor = 9
    RULE_integer = 10
    RULE_op = 11
    RULE_ident = 12

    ruleNames =  [ "program", "stmt_list", "stmt", "assign_stmt", "read_stmt", 
                   "write_stmt", "id_list", "expr_list", "expr", "factor", 
                   "integer", "op", "ident" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    NUMBER=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(tinyParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = tinyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(tinyParser.T__0)
            self.state = 27
            self.stmt_list(0)
            self.state = 28
            self.match(tinyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(tinyParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(tinyParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_stmt_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_list" ):
                listener.enterStmt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_list" ):
                listener.exitStmt_list(self)



    def stmt_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tinyParser.Stmt_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_stmt_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.stmt()
            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tinyParser.Stmt_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                    self.state = 33
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 34
                    self.stmt() 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(tinyParser.Assign_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(tinyParser.Read_stmtContext,0)


        def write_stmt(self):
            return self.getTypedRuleContext(tinyParser.Write_stmtContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = tinyParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tinyParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.assign_stmt()
                pass
            elif token in [tinyParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.read_stmt()
                pass
            elif token in [tinyParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.write_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(tinyParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(tinyParser.ExprContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = tinyParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.ident()
            self.state = 46
            self.match(tinyParser.T__2)
            self.state = 47
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(tinyParser.Id_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_read_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_stmt" ):
                listener.enterRead_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_stmt" ):
                listener.exitRead_stmt(self)




    def read_stmt(self):

        localctx = tinyParser.Read_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(tinyParser.T__3)
            self.state = 50
            self.id_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_list(self):
            return self.getTypedRuleContext(tinyParser.Expr_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_write_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_stmt" ):
                listener.enterWrite_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_stmt" ):
                listener.exitWrite_stmt(self)




    def write_stmt(self):

        localctx = tinyParser.Write_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_write_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(tinyParser.T__4)
            self.state = 53
            self.expr_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(tinyParser.IdentContext,0)


        def id_list(self):
            return self.getTypedRuleContext(tinyParser.Id_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_list" ):
                listener.enterId_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_list" ):
                listener.exitId_list(self)



    def id_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tinyParser.Id_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_id_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.ident()
            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tinyParser.Id_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_id_list)
                    self.state = 58
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 59
                    self.match(tinyParser.T__5)
                    self.state = 60
                    self.ident() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(tinyParser.ExprContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(tinyParser.Expr_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_list" ):
                listener.enterExpr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_list" ):
                listener.exitExpr_list(self)



    def expr_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tinyParser.Expr_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tinyParser.Expr_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_list)
                    self.state = 69
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 70
                    self.match(tinyParser.T__5)
                    self.state = 71
                    self.expr(0) 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(tinyParser.FactorContext,0)


        def expr(self):
            return self.getTypedRuleContext(tinyParser.ExprContext,0)


        def op(self):
            return self.getTypedRuleContext(tinyParser.OpContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tinyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tinyParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 80
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 81
                    self.op()
                    self.state = 82
                    self.factor() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(tinyParser.IdentContext,0)


        def integer(self):
            return self.getTypedRuleContext(tinyParser.IntegerContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = tinyParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tinyParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.ident()
                pass
            elif token in [tinyParser.T__6, tinyParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.integer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(tinyParser.NUMBER, 0)

        def getRuleIndex(self):
            return tinyParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = tinyParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==tinyParser.T__6:
                self.state = 93
                self.match(tinyParser.T__6)


            self.state = 96
            self.match(tinyParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tinyParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = tinyParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==tinyParser.T__6 or _la==tinyParser.T__7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(tinyParser.ID, 0)

        def getRuleIndex(self):
            return tinyParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = tinyParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(tinyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.stmt_list_sempred
        self._predicates[6] = self.id_list_sempred
        self._predicates[7] = self.expr_list_sempred
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def stmt_list_sempred(self, localctx:Stmt_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def id_list_sempred(self, localctx:Id_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_list_sempred(self, localctx:Expr_listContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




