# Generated from xpath.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .xpathParser import xpathParser
else:
    from xpathParser import xpathParser

# This class defines a complete listener for a parse tree produced by xpathParser.
class xpathListener(ParseTreeListener):

    # Enter a parse tree produced by xpathParser#main.
    def enterMain(self, ctx:xpathParser.MainContext):
        pass

    # Exit a parse tree produced by xpathParser#main.
    def exitMain(self, ctx:xpathParser.MainContext):
        pass


    # Enter a parse tree produced by xpathParser#locationPath.
    def enterLocationPath(self, ctx:xpathParser.LocationPathContext):
        pass

    # Exit a parse tree produced by xpathParser#locationPath.
    def exitLocationPath(self, ctx:xpathParser.LocationPathContext):
        pass


    # Enter a parse tree produced by xpathParser#absoluteLocationPathNoroot.
    def enterAbsoluteLocationPathNoroot(self, ctx:xpathParser.AbsoluteLocationPathNorootContext):
        pass

    # Exit a parse tree produced by xpathParser#absoluteLocationPathNoroot.
    def exitAbsoluteLocationPathNoroot(self, ctx:xpathParser.AbsoluteLocationPathNorootContext):
        pass


    # Enter a parse tree produced by xpathParser#relativeLocationPath.
    def enterRelativeLocationPath(self, ctx:xpathParser.RelativeLocationPathContext):
        pass

    # Exit a parse tree produced by xpathParser#relativeLocationPath.
    def exitRelativeLocationPath(self, ctx:xpathParser.RelativeLocationPathContext):
        pass


    # Enter a parse tree produced by xpathParser#step.
    def enterStep(self, ctx:xpathParser.StepContext):
        pass

    # Exit a parse tree produced by xpathParser#step.
    def exitStep(self, ctx:xpathParser.StepContext):
        pass


    # Enter a parse tree produced by xpathParser#axisSpecifier.
    def enterAxisSpecifier(self, ctx:xpathParser.AxisSpecifierContext):
        pass

    # Exit a parse tree produced by xpathParser#axisSpecifier.
    def exitAxisSpecifier(self, ctx:xpathParser.AxisSpecifierContext):
        pass


    # Enter a parse tree produced by xpathParser#nodeTest.
    def enterNodeTest(self, ctx:xpathParser.NodeTestContext):
        pass

    # Exit a parse tree produced by xpathParser#nodeTest.
    def exitNodeTest(self, ctx:xpathParser.NodeTestContext):
        pass


    # Enter a parse tree produced by xpathParser#predicate.
    def enterPredicate(self, ctx:xpathParser.PredicateContext):
        pass

    # Exit a parse tree produced by xpathParser#predicate.
    def exitPredicate(self, ctx:xpathParser.PredicateContext):
        pass


    # Enter a parse tree produced by xpathParser#abbreviatedStep.
    def enterAbbreviatedStep(self, ctx:xpathParser.AbbreviatedStepContext):
        pass

    # Exit a parse tree produced by xpathParser#abbreviatedStep.
    def exitAbbreviatedStep(self, ctx:xpathParser.AbbreviatedStepContext):
        pass


    # Enter a parse tree produced by xpathParser#expr.
    def enterExpr(self, ctx:xpathParser.ExprContext):
        pass

    # Exit a parse tree produced by xpathParser#expr.
    def exitExpr(self, ctx:xpathParser.ExprContext):
        pass


    # Enter a parse tree produced by xpathParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:xpathParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by xpathParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:xpathParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by xpathParser#functionCall.
    def enterFunctionCall(self, ctx:xpathParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by xpathParser#functionCall.
    def exitFunctionCall(self, ctx:xpathParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by xpathParser#unionExprNoRoot.
    def enterUnionExprNoRoot(self, ctx:xpathParser.UnionExprNoRootContext):
        pass

    # Exit a parse tree produced by xpathParser#unionExprNoRoot.
    def exitUnionExprNoRoot(self, ctx:xpathParser.UnionExprNoRootContext):
        pass


    # Enter a parse tree produced by xpathParser#pathExprNoRoot.
    def enterPathExprNoRoot(self, ctx:xpathParser.PathExprNoRootContext):
        pass

    # Exit a parse tree produced by xpathParser#pathExprNoRoot.
    def exitPathExprNoRoot(self, ctx:xpathParser.PathExprNoRootContext):
        pass


    # Enter a parse tree produced by xpathParser#filterExpr.
    def enterFilterExpr(self, ctx:xpathParser.FilterExprContext):
        pass

    # Exit a parse tree produced by xpathParser#filterExpr.
    def exitFilterExpr(self, ctx:xpathParser.FilterExprContext):
        pass


    # Enter a parse tree produced by xpathParser#orExpr.
    def enterOrExpr(self, ctx:xpathParser.OrExprContext):
        pass

    # Exit a parse tree produced by xpathParser#orExpr.
    def exitOrExpr(self, ctx:xpathParser.OrExprContext):
        pass


    # Enter a parse tree produced by xpathParser#andExpr.
    def enterAndExpr(self, ctx:xpathParser.AndExprContext):
        pass

    # Exit a parse tree produced by xpathParser#andExpr.
    def exitAndExpr(self, ctx:xpathParser.AndExprContext):
        pass


    # Enter a parse tree produced by xpathParser#equalityExpr.
    def enterEqualityExpr(self, ctx:xpathParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by xpathParser#equalityExpr.
    def exitEqualityExpr(self, ctx:xpathParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by xpathParser#relationalExpr.
    def enterRelationalExpr(self, ctx:xpathParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by xpathParser#relationalExpr.
    def exitRelationalExpr(self, ctx:xpathParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by xpathParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:xpathParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by xpathParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:xpathParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by xpathParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:xpathParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by xpathParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:xpathParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by xpathParser#unaryExprNoRoot.
    def enterUnaryExprNoRoot(self, ctx:xpathParser.UnaryExprNoRootContext):
        pass

    # Exit a parse tree produced by xpathParser#unaryExprNoRoot.
    def exitUnaryExprNoRoot(self, ctx:xpathParser.UnaryExprNoRootContext):
        pass


    # Enter a parse tree produced by xpathParser#qName.
    def enterQName(self, ctx:xpathParser.QNameContext):
        pass

    # Exit a parse tree produced by xpathParser#qName.
    def exitQName(self, ctx:xpathParser.QNameContext):
        pass


    # Enter a parse tree produced by xpathParser#functionName.
    def enterFunctionName(self, ctx:xpathParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by xpathParser#functionName.
    def exitFunctionName(self, ctx:xpathParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by xpathParser#variableReference.
    def enterVariableReference(self, ctx:xpathParser.VariableReferenceContext):
        pass

    # Exit a parse tree produced by xpathParser#variableReference.
    def exitVariableReference(self, ctx:xpathParser.VariableReferenceContext):
        pass


    # Enter a parse tree produced by xpathParser#nameTest.
    def enterNameTest(self, ctx:xpathParser.NameTestContext):
        pass

    # Exit a parse tree produced by xpathParser#nameTest.
    def exitNameTest(self, ctx:xpathParser.NameTestContext):
        pass


    # Enter a parse tree produced by xpathParser#nCName.
    def enterNCName(self, ctx:xpathParser.NCNameContext):
        pass

    # Exit a parse tree produced by xpathParser#nCName.
    def exitNCName(self, ctx:xpathParser.NCNameContext):
        pass



del xpathParser