# Generated from tinyc.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\60\n\3\f\3\16\3\63\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5E\n\5\3\6\3\6\3\6\3\6\3\6\5\6L\n\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7W\n\7\f\7\16\7Z")
        buf.write("\13\7\3\b\3\b\3\b\5\b_\n\b\3\t\3\t\3\n\3\n\3\n\2\3\f\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\2\2i\2\25\3\2\2\2\49\3\2\2\2\6")
        buf.write(";\3\2\2\2\bD\3\2\2\2\nK\3\2\2\2\fM\3\2\2\2\16^\3\2\2\2")
        buf.write("\20`\3\2\2\2\22b\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26")
        buf.write("\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31")
        buf.write("\32\7\3\2\2\32\33\5\6\4\2\33\34\5\4\3\2\34:\3\2\2\2\35")
        buf.write("\36\7\3\2\2\36\37\5\6\4\2\37 \5\4\3\2 !\7\4\2\2!\"\5\4")
        buf.write("\3\2\":\3\2\2\2#$\7\5\2\2$%\5\6\4\2%&\5\4\3\2&:\3\2\2")
        buf.write("\2\'(\7\6\2\2()\5\4\3\2)*\7\5\2\2*+\5\6\4\2+,\7\7\2\2")
        buf.write(",:\3\2\2\2-\61\7\b\2\2.\60\5\4\3\2/.\3\2\2\2\60\63\3\2")
        buf.write("\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2")
        buf.write("\2\2\64:\7\t\2\2\65\66\5\b\5\2\66\67\7\7\2\2\67:\3\2\2")
        buf.write("\28:\7\7\2\29\31\3\2\2\29\35\3\2\2\29#\3\2\2\29\'\3\2")
        buf.write("\2\29-\3\2\2\29\65\3\2\2\298\3\2\2\2:\5\3\2\2\2;<\7\n")
        buf.write("\2\2<=\5\b\5\2=>\7\13\2\2>\7\3\2\2\2?E\5\n\6\2@A\5\20")
        buf.write("\t\2AB\7\f\2\2BC\5\b\5\2CE\3\2\2\2D?\3\2\2\2D@\3\2\2\2")
        buf.write("E\t\3\2\2\2FL\5\f\7\2GH\5\f\7\2HI\7\r\2\2IJ\5\f\7\2JL")
        buf.write("\3\2\2\2KF\3\2\2\2KG\3\2\2\2L\13\3\2\2\2MN\b\7\1\2NO\5")
        buf.write("\16\b\2OX\3\2\2\2PQ\f\4\2\2QR\7\16\2\2RW\5\16\b\2ST\f")
        buf.write("\3\2\2TU\7\17\2\2UW\5\16\b\2VP\3\2\2\2VS\3\2\2\2WZ\3\2")
        buf.write("\2\2XV\3\2\2\2XY\3\2\2\2Y\r\3\2\2\2ZX\3\2\2\2[_\5\20\t")
        buf.write("\2\\_\5\22\n\2]_\5\6\4\2^[\3\2\2\2^\\\3\2\2\2^]\3\2\2")
        buf.write("\2_\17\3\2\2\2`a\7\20\2\2a\21\3\2\2\2bc\7\21\2\2c\23\3")
        buf.write("\2\2\2\n\27\619DKVX^")
        return buf.getvalue()


class tinycParser ( Parser ):

    grammarFileName = "tinyc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'do'", "';'", 
                     "'{'", "'}'", "'('", "')'", "'='", "'<'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_paren_expr = 2
    RULE_expr = 3
    RULE_test = 4
    RULE_sum_ = 5
    RULE_term = 6
    RULE_id_ = 7
    RULE_integer = 8

    ruleNames =  [ "program", "statement", "paren_expr", "expr", "test", 
                   "sum_", "term", "id_", "integer" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    STRING=14
    INT=15
    WS=16

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinycParser.StatementContext)
            else:
                return self.getTypedRuleContext(tinycParser.StatementContext,i)


        def getRuleIndex(self):
            return tinycParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = tinycParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tinycParser.T__0) | (1 << tinycParser.T__2) | (1 << tinycParser.T__3) | (1 << tinycParser.T__4) | (1 << tinycParser.T__5) | (1 << tinycParser.T__7) | (1 << tinycParser.STRING) | (1 << tinycParser.INT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paren_expr(self):
            return self.getTypedRuleContext(tinycParser.Paren_exprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinycParser.StatementContext)
            else:
                return self.getTypedRuleContext(tinycParser.StatementContext,i)


        def expr(self):
            return self.getTypedRuleContext(tinycParser.ExprContext,0)


        def getRuleIndex(self):
            return tinycParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = tinycParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(tinycParser.T__0)
                self.state = 24
                self.paren_expr()
                self.state = 25
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(tinycParser.T__0)
                self.state = 28
                self.paren_expr()
                self.state = 29
                self.statement()
                self.state = 30
                self.match(tinycParser.T__1)
                self.state = 31
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.match(tinycParser.T__2)
                self.state = 34
                self.paren_expr()
                self.state = 35
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(tinycParser.T__3)
                self.state = 38
                self.statement()
                self.state = 39
                self.match(tinycParser.T__2)
                self.state = 40
                self.paren_expr()
                self.state = 41
                self.match(tinycParser.T__4)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(tinycParser.T__5)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tinycParser.T__0) | (1 << tinycParser.T__2) | (1 << tinycParser.T__3) | (1 << tinycParser.T__4) | (1 << tinycParser.T__5) | (1 << tinycParser.T__7) | (1 << tinycParser.STRING) | (1 << tinycParser.INT))) != 0):
                    self.state = 44
                    self.statement()
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(tinycParser.T__6)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.expr()
                self.state = 52
                self.match(tinycParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.match(tinycParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paren_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(tinycParser.ExprContext,0)


        def getRuleIndex(self):
            return tinycParser.RULE_paren_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen_expr" ):
                listener.enterParen_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen_expr" ):
                listener.exitParen_expr(self)




    def paren_expr(self):

        localctx = tinycParser.Paren_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paren_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(tinycParser.T__7)
            self.state = 58
            self.expr()
            self.state = 59
            self.match(tinycParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(tinycParser.TestContext,0)


        def id_(self):
            return self.getTypedRuleContext(tinycParser.Id_Context,0)


        def expr(self):
            return self.getTypedRuleContext(tinycParser.ExprContext,0)


        def getRuleIndex(self):
            return tinycParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = tinycParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.test()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.id_()
                self.state = 63
                self.match(tinycParser.T__9)
                self.state = 64
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sum_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinycParser.Sum_Context)
            else:
                return self.getTypedRuleContext(tinycParser.Sum_Context,i)


        def getRuleIndex(self):
            return tinycParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)




    def test(self):

        localctx = tinycParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_test)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.sum_(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.sum_(0)
                self.state = 70
                self.match(tinycParser.T__10)
                self.state = 71
                self.sum_(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sum_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(tinycParser.TermContext,0)


        def sum_(self):
            return self.getTypedRuleContext(tinycParser.Sum_Context,0)


        def getRuleIndex(self):
            return tinycParser.RULE_sum_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum_" ):
                listener.enterSum_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum_" ):
                listener.exitSum_(self)



    def sum_(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tinycParser.Sum_Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_sum_, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = tinycParser.Sum_Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sum_)
                        self.state = 78
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 79
                        self.match(tinycParser.T__11)
                        self.state = 80
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = tinycParser.Sum_Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sum_)
                        self.state = 81
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 82
                        self.match(tinycParser.T__12)
                        self.state = 83
                        self.term()
                        pass

             
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(tinycParser.Id_Context,0)


        def integer(self):
            return self.getTypedRuleContext(tinycParser.IntegerContext,0)


        def paren_expr(self):
            return self.getTypedRuleContext(tinycParser.Paren_exprContext,0)


        def getRuleIndex(self):
            return tinycParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = tinycParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tinycParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.id_()
                pass
            elif token in [tinycParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.integer()
                pass
            elif token in [tinycParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.paren_expr()
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


    class Id_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(tinycParser.STRING, 0)

        def getRuleIndex(self):
            return tinycParser.RULE_id_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_" ):
                listener.enterId_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_" ):
                listener.exitId_(self)




    def id_(self):

        localctx = tinycParser.Id_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_id_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(tinycParser.STRING)
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

        def INT(self):
            return self.getToken(tinycParser.INT, 0)

        def getRuleIndex(self):
            return tinycParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = tinycParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(tinycParser.INT)
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
        self._predicates[5] = self.sum__sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sum__sempred(self, localctx:Sum_Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




