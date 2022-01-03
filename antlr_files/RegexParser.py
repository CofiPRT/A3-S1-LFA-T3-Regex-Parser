# Generated from E:/RANDOM/WORKSPACE/ANUL3/SEM1/LFA/Tema3/antlr_files\Regex.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\5\3\33")
        buf.write("\n\3\3\4\3\4\5\4\37\n\4\3\5\3\5\5\5#\n\5\3\6\3\6\5\6\'")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2")
        buf.write("\2\2\62\2\26\3\2\2\2\4\32\3\2\2\2\6\36\3\2\2\2\b\"\3\2")
        buf.write("\2\2\n&\3\2\2\2\f(\3\2\2\2\16,\3\2\2\2\20/\3\2\2\2\22")
        buf.write("\62\3\2\2\2\24\66\3\2\2\2\26\27\5\4\3\2\27\3\3\2\2\2\30")
        buf.write("\33\5\6\4\2\31\33\5\f\7\2\32\30\3\2\2\2\32\31\3\2\2\2")
        buf.write("\33\5\3\2\2\2\34\37\5\b\5\2\35\37\5\16\b\2\36\34\3\2\2")
        buf.write("\2\36\35\3\2\2\2\37\7\3\2\2\2 #\5\n\6\2!#\5\20\t\2\" ")
        buf.write("\3\2\2\2\"!\3\2\2\2#\t\3\2\2\2$\'\5\22\n\2%\'\5\24\13")
        buf.write("\2&$\3\2\2\2&%\3\2\2\2\'\13\3\2\2\2()\5\6\4\2)*\7\6\2")
        buf.write("\2*+\5\4\3\2+\r\3\2\2\2,-\5\b\5\2-.\5\6\4\2.\17\3\2\2")
        buf.write("\2/\60\5\n\6\2\60\61\7\5\2\2\61\21\3\2\2\2\62\63\7\3\2")
        buf.write("\2\63\64\5\2\2\2\64\65\7\4\2\2\65\23\3\2\2\2\66\67\7\7")
        buf.write("\2\2\67\25\3\2\2\2\6\32\36\"&")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'|'" ]

    symbolicNames = [ "<INVALID>", "PARENTHESIS_OPEN", "PARENTHESIS_CLOSE", 
                      "KLEENE_STAR", "UNION", "SYMBOL" ]

    RULE_expr = 0
    RULE_precedence1 = 1
    RULE_precedence2 = 2
    RULE_precedence3 = 3
    RULE_precedence4 = 4
    RULE_union = 5
    RULE_concat = 6
    RULE_kleene = 7
    RULE_parentheses = 8
    RULE_symbol = 9

    ruleNames =  [ "expr", "precedence1", "precedence2", "precedence3", 
                   "precedence4", "union", "concat", "kleene", "parentheses", 
                   "symbol" ]

    EOF = Token.EOF
    PARENTHESIS_OPEN=1
    PARENTHESIS_CLOSE=2
    KLEENE_STAR=3
    UNION=4
    SYMBOL=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence1(self):
            return self.getTypedRuleContext(RegexParser.Precedence1Context,0)


        def getRuleIndex(self):
            return RegexParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = RegexParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.precedence1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Precedence1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence2(self):
            return self.getTypedRuleContext(RegexParser.Precedence2Context,0)


        def union(self):
            return self.getTypedRuleContext(RegexParser.UnionContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_precedence1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence1" ):
                listener.enterPrecedence1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence1" ):
                listener.exitPrecedence1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence1" ):
                return visitor.visitPrecedence1(self)
            else:
                return visitor.visitChildren(self)




    def precedence1(self):

        localctx = RegexParser.Precedence1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_precedence1)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.precedence2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.union()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Precedence2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence3(self):
            return self.getTypedRuleContext(RegexParser.Precedence3Context,0)


        def concat(self):
            return self.getTypedRuleContext(RegexParser.ConcatContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_precedence2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence2" ):
                listener.enterPrecedence2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence2" ):
                listener.exitPrecedence2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence2" ):
                return visitor.visitPrecedence2(self)
            else:
                return visitor.visitChildren(self)




    def precedence2(self):

        localctx = RegexParser.Precedence2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_precedence2)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.precedence3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.concat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Precedence3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence4(self):
            return self.getTypedRuleContext(RegexParser.Precedence4Context,0)


        def kleene(self):
            return self.getTypedRuleContext(RegexParser.KleeneContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_precedence3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence3" ):
                listener.enterPrecedence3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence3" ):
                listener.exitPrecedence3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence3" ):
                return visitor.visitPrecedence3(self)
            else:
                return visitor.visitChildren(self)




    def precedence3(self):

        localctx = RegexParser.Precedence3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_precedence3)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.precedence4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.kleene()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Precedence4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parentheses(self):
            return self.getTypedRuleContext(RegexParser.ParenthesesContext,0)


        def symbol(self):
            return self.getTypedRuleContext(RegexParser.SymbolContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_precedence4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence4" ):
                listener.enterPrecedence4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence4" ):
                listener.exitPrecedence4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence4" ):
                return visitor.visitPrecedence4(self)
            else:
                return visitor.visitChildren(self)




    def precedence4(self):

        localctx = RegexParser.Precedence4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_precedence4)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.PARENTHESIS_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.parentheses()
                pass
            elif token in [RegexParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.symbol()
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


    class UnionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence2(self):
            return self.getTypedRuleContext(RegexParser.Precedence2Context,0)


        def UNION(self):
            return self.getToken(RegexParser.UNION, 0)

        def precedence1(self):
            return self.getTypedRuleContext(RegexParser.Precedence1Context,0)


        def getRuleIndex(self):
            return RegexParser.RULE_union

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion" ):
                listener.enterUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion" ):
                listener.exitUnion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion" ):
                return visitor.visitUnion(self)
            else:
                return visitor.visitChildren(self)




    def union(self):

        localctx = RegexParser.UnionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_union)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.precedence2()
            self.state = 39
            self.match(RegexParser.UNION)
            self.state = 40
            self.precedence1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence3(self):
            return self.getTypedRuleContext(RegexParser.Precedence3Context,0)


        def precedence2(self):
            return self.getTypedRuleContext(RegexParser.Precedence2Context,0)


        def getRuleIndex(self):
            return RegexParser.RULE_concat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)




    def concat(self):

        localctx = RegexParser.ConcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_concat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.precedence3()
            self.state = 43
            self.precedence2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KleeneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence4(self):
            return self.getTypedRuleContext(RegexParser.Precedence4Context,0)


        def KLEENE_STAR(self):
            return self.getToken(RegexParser.KLEENE_STAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_kleene

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKleene" ):
                listener.enterKleene(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKleene" ):
                listener.exitKleene(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKleene" ):
                return visitor.visitKleene(self)
            else:
                return visitor.visitChildren(self)




    def kleene(self):

        localctx = RegexParser.KleeneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_kleene)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.precedence4()
            self.state = 46
            self.match(RegexParser.KLEENE_STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenthesesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTHESIS_OPEN(self):
            return self.getToken(RegexParser.PARENTHESIS_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def PARENTHESIS_CLOSE(self):
            return self.getToken(RegexParser.PARENTHESIS_CLOSE, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_parentheses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)




    def parentheses(self):

        localctx = RegexParser.ParenthesesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parentheses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(RegexParser.PARENTHESIS_OPEN)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(RegexParser.PARENTHESIS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self):
            return self.getToken(RegexParser.SYMBOL, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = RegexParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(RegexParser.SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





