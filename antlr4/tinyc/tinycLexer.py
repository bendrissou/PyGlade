# Generated from tinyc.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\6\17H\n\17\r\17\16\17I\3\20\6")
        buf.write("\20M\n\20\r\20\16\20N\3\21\3\21\3\21\3\21\2\2\22\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22\3\2\5\3\2c|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2U\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3")
        buf.write("\2\2\2\5&\3\2\2\2\7+\3\2\2\2\t\61\3\2\2\2\13\64\3\2\2")
        buf.write("\2\r\66\3\2\2\2\178\3\2\2\2\21:\3\2\2\2\23<\3\2\2\2\25")
        buf.write(">\3\2\2\2\27@\3\2\2\2\31B\3\2\2\2\33D\3\2\2\2\35G\3\2")
        buf.write("\2\2\37L\3\2\2\2!P\3\2\2\2#$\7k\2\2$%\7h\2\2%\4\3\2\2")
        buf.write("\2&\'\7g\2\2\'(\7n\2\2()\7u\2\2)*\7g\2\2*\6\3\2\2\2+,")
        buf.write("\7y\2\2,-\7j\2\2-.\7k\2\2./\7n\2\2/\60\7g\2\2\60\b\3\2")
        buf.write("\2\2\61\62\7f\2\2\62\63\7q\2\2\63\n\3\2\2\2\64\65\7=\2")
        buf.write("\2\65\f\3\2\2\2\66\67\7}\2\2\67\16\3\2\2\289\7\177\2\2")
        buf.write("9\20\3\2\2\2:;\7*\2\2;\22\3\2\2\2<=\7+\2\2=\24\3\2\2\2")
        buf.write(">?\7?\2\2?\26\3\2\2\2@A\7>\2\2A\30\3\2\2\2BC\7-\2\2C\32")
        buf.write("\3\2\2\2DE\7/\2\2E\34\3\2\2\2FH\t\2\2\2GF\3\2\2\2HI\3")
        buf.write("\2\2\2IG\3\2\2\2IJ\3\2\2\2J\36\3\2\2\2KM\t\3\2\2LK\3\2")
        buf.write("\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2O \3\2\2\2PQ\t\4\2\2")
        buf.write("QR\3\2\2\2RS\b\21\2\2S\"\3\2\2\2\5\2IN\3\b\2\2")
        return buf.getvalue()


class tinycLexer(Lexer):

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
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    STRING = 14
    INT = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'while'", "'do'", "';'", "'{'", "'}'", "'('", 
            "')'", "'='", "'<'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "STRING", 
                  "INT", "WS" ]

    grammarFileName = "tinyc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


