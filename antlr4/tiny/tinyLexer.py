# Generated from tiny.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\6\n9\n\n\r\n\16\n:\3\13\6\13>\n\13\r\13\16\13?\3")
        buf.write("\f\3\f\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\3\2\4\4\2C\\c|\5\2\f\f\17\17\"\"\2")
        buf.write("F\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\37\3\2")
        buf.write("\2\2\7#\3\2\2\2\t&\3\2\2\2\13+\3\2\2\2\r\61\3\2\2\2\17")
        buf.write("\63\3\2\2\2\21\65\3\2\2\2\238\3\2\2\2\25=\3\2\2\2\27A")
        buf.write("\3\2\2\2\31\32\7D\2\2\32\33\7G\2\2\33\34\7I\2\2\34\35")
        buf.write("\7K\2\2\35\36\7P\2\2\36\4\3\2\2\2\37 \7G\2\2 !\7P\2\2")
        buf.write("!\"\7F\2\2\"\6\3\2\2\2#$\7<\2\2$%\7?\2\2%\b\3\2\2\2&\'")
        buf.write("\7T\2\2\'(\7G\2\2()\7C\2\2)*\7F\2\2*\n\3\2\2\2+,\7Y\2")
        buf.write("\2,-\7T\2\2-.\7K\2\2./\7V\2\2/\60\7G\2\2\60\f\3\2\2\2")
        buf.write("\61\62\7.\2\2\62\16\3\2\2\2\63\64\7/\2\2\64\20\3\2\2\2")
        buf.write("\65\66\7-\2\2\66\22\3\2\2\2\679\t\2\2\28\67\3\2\2\29:")
        buf.write("\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\24\3\2\2\2<>\4\62;\2=<\3")
        buf.write("\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\26\3\2\2\2AB\t\3")
        buf.write("\2\2BC\3\2\2\2CD\b\f\2\2D\30\3\2\2\2\5\2:?\3\b\2\2")
        return buf.getvalue()


class tinyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    ID = 9
    NUMBER = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'BEGIN'", "'END'", "':='", "'READ'", "'WRITE'", "','", "'-'", 
            "'+'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "ID", "NUMBER", "WS" ]

    grammarFileName = "tiny.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


