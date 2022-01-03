# Generated from E:/RANDOM/WORKSPACE/ANUL3/SEM1/LFA/Tema3/antlr_files\Regex.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\32\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write("\2\3\3\3\3\3\4\6\4\23\n\4\r\4\16\4\24\3\5\3\5\3\6\3\6")
        buf.write("\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\3\3\2c|\2\32\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3")
        buf.write("\r\3\2\2\2\5\17\3\2\2\2\7\22\3\2\2\2\t\26\3\2\2\2\13\30")
        buf.write("\3\2\2\2\r\16\7*\2\2\16\4\3\2\2\2\17\20\7+\2\2\20\6\3")
        buf.write("\2\2\2\21\23\7,\2\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22")
        buf.write("\3\2\2\2\24\25\3\2\2\2\25\b\3\2\2\2\26\27\7~\2\2\27\n")
        buf.write("\3\2\2\2\30\31\t\2\2\2\31\f\3\2\2\2\4\2\24\2")
        return buf.getvalue()


class RegexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PARENTHESIS_OPEN = 1
    PARENTHESIS_CLOSE = 2
    KLEENE_STAR = 3
    UNION = 4
    SYMBOL = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "PARENTHESIS_OPEN", "PARENTHESIS_CLOSE", "KLEENE_STAR", "UNION", 
            "SYMBOL" ]

    ruleNames = [ "PARENTHESIS_OPEN", "PARENTHESIS_CLOSE", "KLEENE_STAR", 
                  "UNION", "SYMBOL" ]

    grammarFileName = "Regex.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


