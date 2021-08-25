# Generated from pascal.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pascalParser import pascalParser
else:
    from pascalParser import pascalParser

# This class defines a complete listener for a parse tree produced by pascalParser.
class pascalListener(ParseTreeListener):

    # Enter a parse tree produced by pascalParser#program.
    def enterProgram(self, ctx:pascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by pascalParser#program.
    def exitProgram(self, ctx:pascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by pascalParser#programHeading.
    def enterProgramHeading(self, ctx:pascalParser.ProgramHeadingContext):
        pass

    # Exit a parse tree produced by pascalParser#programHeading.
    def exitProgramHeading(self, ctx:pascalParser.ProgramHeadingContext):
        pass


    # Enter a parse tree produced by pascalParser#identifier.
    def enterIdentifier(self, ctx:pascalParser.IdentifierContext):
        pass

    # Exit a parse tree produced by pascalParser#identifier.
    def exitIdentifier(self, ctx:pascalParser.IdentifierContext):
        pass


    # Enter a parse tree produced by pascalParser#block.
    def enterBlock(self, ctx:pascalParser.BlockContext):
        pass

    # Exit a parse tree produced by pascalParser#block.
    def exitBlock(self, ctx:pascalParser.BlockContext):
        pass


    # Enter a parse tree produced by pascalParser#usesUnitsPart.
    def enterUsesUnitsPart(self, ctx:pascalParser.UsesUnitsPartContext):
        pass

    # Exit a parse tree produced by pascalParser#usesUnitsPart.
    def exitUsesUnitsPart(self, ctx:pascalParser.UsesUnitsPartContext):
        pass


    # Enter a parse tree produced by pascalParser#labelDeclarationPart.
    def enterLabelDeclarationPart(self, ctx:pascalParser.LabelDeclarationPartContext):
        pass

    # Exit a parse tree produced by pascalParser#labelDeclarationPart.
    def exitLabelDeclarationPart(self, ctx:pascalParser.LabelDeclarationPartContext):
        pass


    # Enter a parse tree produced by pascalParser#label.
    def enterLabel(self, ctx:pascalParser.LabelContext):
        pass

    # Exit a parse tree produced by pascalParser#label.
    def exitLabel(self, ctx:pascalParser.LabelContext):
        pass


    # Enter a parse tree produced by pascalParser#constantDefinitionPart.
    def enterConstantDefinitionPart(self, ctx:pascalParser.ConstantDefinitionPartContext):
        pass

    # Exit a parse tree produced by pascalParser#constantDefinitionPart.
    def exitConstantDefinitionPart(self, ctx:pascalParser.ConstantDefinitionPartContext):
        pass


    # Enter a parse tree produced by pascalParser#constantDefinition.
    def enterConstantDefinition(self, ctx:pascalParser.ConstantDefinitionContext):
        pass

    # Exit a parse tree produced by pascalParser#constantDefinition.
    def exitConstantDefinition(self, ctx:pascalParser.ConstantDefinitionContext):
        pass


    # Enter a parse tree produced by pascalParser#constantChr.
    def enterConstantChr(self, ctx:pascalParser.ConstantChrContext):
        pass

    # Exit a parse tree produced by pascalParser#constantChr.
    def exitConstantChr(self, ctx:pascalParser.ConstantChrContext):
        pass


    # Enter a parse tree produced by pascalParser#constant.
    def enterConstant(self, ctx:pascalParser.ConstantContext):
        pass

    # Exit a parse tree produced by pascalParser#constant.
    def exitConstant(self, ctx:pascalParser.ConstantContext):
        pass


    # Enter a parse tree produced by pascalParser#unsignedNumber.
    def enterUnsignedNumber(self, ctx:pascalParser.UnsignedNumberContext):
        pass

    # Exit a parse tree produced by pascalParser#unsignedNumber.
    def exitUnsignedNumber(self, ctx:pascalParser.UnsignedNumberContext):
        pass


    # Enter a parse tree produced by pascalParser#unsignedInteger.
    def enterUnsignedInteger(self, ctx:pascalParser.UnsignedIntegerContext):
        pass

    # Exit a parse tree produced by pascalParser#unsignedInteger.
    def exitUnsignedInteger(self, ctx:pascalParser.UnsignedIntegerContext):
        pass


    # Enter a parse tree produced by pascalParser#unsignedReal.
    def enterUnsignedReal(self, ctx:pascalParser.UnsignedRealContext):
        pass

    # Exit a parse tree produced by pascalParser#unsignedReal.
    def exitUnsignedReal(self, ctx:pascalParser.UnsignedRealContext):
        pass


    # Enter a parse tree produced by pascalParser#sign.
    def enterSign(self, ctx:pascalParser.SignContext):
        pass

    # Exit a parse tree produced by pascalParser#sign.
    def exitSign(self, ctx:pascalParser.SignContext):
        pass


    # Enter a parse tree produced by pascalParser#bool_.
    def enterBool_(self, ctx:pascalParser.Bool_Context):
        pass

    # Exit a parse tree produced by pascalParser#bool_.
    def exitBool_(self, ctx:pascalParser.Bool_Context):
        pass


    # Enter a parse tree produced by pascalParser#string.
    def enterString(self, ctx:pascalParser.StringContext):
        pass

    # Exit a parse tree produced by pascalParser#string.
    def exitString(self, ctx:pascalParser.StringContext):
        pass


    # Enter a parse tree produced by pascalParser#typeDefinitionPart.
    def enterTypeDefinitionPart(self, ctx:pascalParser.TypeDefinitionPartContext):
        pass

    # Exit a parse tree produced by pascalParser#typeDefinitionPart.
    def exitTypeDefinitionPart(self, ctx:pascalParser.TypeDefinitionPartContext):
        pass


    # Enter a parse tree produced by pascalParser#typeDefinition.
    def enterTypeDefinition(self, ctx:pascalParser.TypeDefinitionContext):
        pass

    # Exit a parse tree produced by pascalParser#typeDefinition.
    def exitTypeDefinition(self, ctx:pascalParser.TypeDefinitionContext):
        pass


    # Enter a parse tree produced by pascalParser#functionType.
    def enterFunctionType(self, ctx:pascalParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#functionType.
    def exitFunctionType(self, ctx:pascalParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#procedureType.
    def enterProcedureType(self, ctx:pascalParser.ProcedureTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureType.
    def exitProcedureType(self, ctx:pascalParser.ProcedureTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#type_.
    def enterType_(self, ctx:pascalParser.Type_Context):
        pass

    # Exit a parse tree produced by pascalParser#type_.
    def exitType_(self, ctx:pascalParser.Type_Context):
        pass


    # Enter a parse tree produced by pascalParser#simpleType.
    def enterSimpleType(self, ctx:pascalParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#simpleType.
    def exitSimpleType(self, ctx:pascalParser.SimpleTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#scalarType.
    def enterScalarType(self, ctx:pascalParser.ScalarTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#scalarType.
    def exitScalarType(self, ctx:pascalParser.ScalarTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#subrangeType.
    def enterSubrangeType(self, ctx:pascalParser.SubrangeTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#subrangeType.
    def exitSubrangeType(self, ctx:pascalParser.SubrangeTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#typeIdentifier.
    def enterTypeIdentifier(self, ctx:pascalParser.TypeIdentifierContext):
        pass

    # Exit a parse tree produced by pascalParser#typeIdentifier.
    def exitTypeIdentifier(self, ctx:pascalParser.TypeIdentifierContext):
        pass


    # Enter a parse tree produced by pascalParser#structuredType.
    def enterStructuredType(self, ctx:pascalParser.StructuredTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#structuredType.
    def exitStructuredType(self, ctx:pascalParser.StructuredTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#unpackedStructuredType.
    def enterUnpackedStructuredType(self, ctx:pascalParser.UnpackedStructuredTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#unpackedStructuredType.
    def exitUnpackedStructuredType(self, ctx:pascalParser.UnpackedStructuredTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#stringtype.
    def enterStringtype(self, ctx:pascalParser.StringtypeContext):
        pass

    # Exit a parse tree produced by pascalParser#stringtype.
    def exitStringtype(self, ctx:pascalParser.StringtypeContext):
        pass


    # Enter a parse tree produced by pascalParser#arrayType.
    def enterArrayType(self, ctx:pascalParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#arrayType.
    def exitArrayType(self, ctx:pascalParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#typeList.
    def enterTypeList(self, ctx:pascalParser.TypeListContext):
        pass

    # Exit a parse tree produced by pascalParser#typeList.
    def exitTypeList(self, ctx:pascalParser.TypeListContext):
        pass


    # Enter a parse tree produced by pascalParser#indexType.
    def enterIndexType(self, ctx:pascalParser.IndexTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#indexType.
    def exitIndexType(self, ctx:pascalParser.IndexTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#componentType.
    def enterComponentType(self, ctx:pascalParser.ComponentTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#componentType.
    def exitComponentType(self, ctx:pascalParser.ComponentTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#recordType.
    def enterRecordType(self, ctx:pascalParser.RecordTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#recordType.
    def exitRecordType(self, ctx:pascalParser.RecordTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#fieldList.
    def enterFieldList(self, ctx:pascalParser.FieldListContext):
        pass

    # Exit a parse tree produced by pascalParser#fieldList.
    def exitFieldList(self, ctx:pascalParser.FieldListContext):
        pass


    # Enter a parse tree produced by pascalParser#fixedPart.
    def enterFixedPart(self, ctx:pascalParser.FixedPartContext):
        pass

    # Exit a parse tree produced by pascalParser#fixedPart.
    def exitFixedPart(self, ctx:pascalParser.FixedPartContext):
        pass


    # Enter a parse tree produced by pascalParser#recordSection.
    def enterRecordSection(self, ctx:pascalParser.RecordSectionContext):
        pass

    # Exit a parse tree produced by pascalParser#recordSection.
    def exitRecordSection(self, ctx:pascalParser.RecordSectionContext):
        pass


    # Enter a parse tree produced by pascalParser#variantPart.
    def enterVariantPart(self, ctx:pascalParser.VariantPartContext):
        pass

    # Exit a parse tree produced by pascalParser#variantPart.
    def exitVariantPart(self, ctx:pascalParser.VariantPartContext):
        pass


    # Enter a parse tree produced by pascalParser#tag.
    def enterTag(self, ctx:pascalParser.TagContext):
        pass

    # Exit a parse tree produced by pascalParser#tag.
    def exitTag(self, ctx:pascalParser.TagContext):
        pass


    # Enter a parse tree produced by pascalParser#variant.
    def enterVariant(self, ctx:pascalParser.VariantContext):
        pass

    # Exit a parse tree produced by pascalParser#variant.
    def exitVariant(self, ctx:pascalParser.VariantContext):
        pass


    # Enter a parse tree produced by pascalParser#setType.
    def enterSetType(self, ctx:pascalParser.SetTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#setType.
    def exitSetType(self, ctx:pascalParser.SetTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#baseType.
    def enterBaseType(self, ctx:pascalParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#baseType.
    def exitBaseType(self, ctx:pascalParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#fileType.
    def enterFileType(self, ctx:pascalParser.FileTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#fileType.
    def exitFileType(self, ctx:pascalParser.FileTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#pointerType.
    def enterPointerType(self, ctx:pascalParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#pointerType.
    def exitPointerType(self, ctx:pascalParser.PointerTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#variableDeclarationPart.
    def enterVariableDeclarationPart(self, ctx:pascalParser.VariableDeclarationPartContext):
        pass

    # Exit a parse tree produced by pascalParser#variableDeclarationPart.
    def exitVariableDeclarationPart(self, ctx:pascalParser.VariableDeclarationPartContext):
        pass


    # Enter a parse tree produced by pascalParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:pascalParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by pascalParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:pascalParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by pascalParser#procedureAndFunctionDeclarationPart.
    def enterProcedureAndFunctionDeclarationPart(self, ctx:pascalParser.ProcedureAndFunctionDeclarationPartContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureAndFunctionDeclarationPart.
    def exitProcedureAndFunctionDeclarationPart(self, ctx:pascalParser.ProcedureAndFunctionDeclarationPartContext):
        pass


    # Enter a parse tree produced by pascalParser#procedureOrFunctionDeclaration.
    def enterProcedureOrFunctionDeclaration(self, ctx:pascalParser.ProcedureOrFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureOrFunctionDeclaration.
    def exitProcedureOrFunctionDeclaration(self, ctx:pascalParser.ProcedureOrFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by pascalParser#procedureDeclaration.
    def enterProcedureDeclaration(self, ctx:pascalParser.ProcedureDeclarationContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureDeclaration.
    def exitProcedureDeclaration(self, ctx:pascalParser.ProcedureDeclarationContext):
        pass


    # Enter a parse tree produced by pascalParser#formalParameterList.
    def enterFormalParameterList(self, ctx:pascalParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by pascalParser#formalParameterList.
    def exitFormalParameterList(self, ctx:pascalParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by pascalParser#formalParameterSection.
    def enterFormalParameterSection(self, ctx:pascalParser.FormalParameterSectionContext):
        pass

    # Exit a parse tree produced by pascalParser#formalParameterSection.
    def exitFormalParameterSection(self, ctx:pascalParser.FormalParameterSectionContext):
        pass


    # Enter a parse tree produced by pascalParser#parameterGroup.
    def enterParameterGroup(self, ctx:pascalParser.ParameterGroupContext):
        pass

    # Exit a parse tree produced by pascalParser#parameterGroup.
    def exitParameterGroup(self, ctx:pascalParser.ParameterGroupContext):
        pass


    # Enter a parse tree produced by pascalParser#identifierList.
    def enterIdentifierList(self, ctx:pascalParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by pascalParser#identifierList.
    def exitIdentifierList(self, ctx:pascalParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by pascalParser#constList.
    def enterConstList(self, ctx:pascalParser.ConstListContext):
        pass

    # Exit a parse tree produced by pascalParser#constList.
    def exitConstList(self, ctx:pascalParser.ConstListContext):
        pass


    # Enter a parse tree produced by pascalParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:pascalParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by pascalParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:pascalParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by pascalParser#resultType.
    def enterResultType(self, ctx:pascalParser.ResultTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#resultType.
    def exitResultType(self, ctx:pascalParser.ResultTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#statement.
    def enterStatement(self, ctx:pascalParser.StatementContext):
        pass

    # Exit a parse tree produced by pascalParser#statement.
    def exitStatement(self, ctx:pascalParser.StatementContext):
        pass


    # Enter a parse tree produced by pascalParser#unlabelledStatement.
    def enterUnlabelledStatement(self, ctx:pascalParser.UnlabelledStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#unlabelledStatement.
    def exitUnlabelledStatement(self, ctx:pascalParser.UnlabelledStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#simpleStatement.
    def enterSimpleStatement(self, ctx:pascalParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#simpleStatement.
    def exitSimpleStatement(self, ctx:pascalParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:pascalParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:pascalParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#variable.
    def enterVariable(self, ctx:pascalParser.VariableContext):
        pass

    # Exit a parse tree produced by pascalParser#variable.
    def exitVariable(self, ctx:pascalParser.VariableContext):
        pass


    # Enter a parse tree produced by pascalParser#expression.
    def enterExpression(self, ctx:pascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pascalParser#expression.
    def exitExpression(self, ctx:pascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pascalParser#relationaloperator.
    def enterRelationaloperator(self, ctx:pascalParser.RelationaloperatorContext):
        pass

    # Exit a parse tree produced by pascalParser#relationaloperator.
    def exitRelationaloperator(self, ctx:pascalParser.RelationaloperatorContext):
        pass


    # Enter a parse tree produced by pascalParser#simpleExpression.
    def enterSimpleExpression(self, ctx:pascalParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by pascalParser#simpleExpression.
    def exitSimpleExpression(self, ctx:pascalParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by pascalParser#additiveoperator.
    def enterAdditiveoperator(self, ctx:pascalParser.AdditiveoperatorContext):
        pass

    # Exit a parse tree produced by pascalParser#additiveoperator.
    def exitAdditiveoperator(self, ctx:pascalParser.AdditiveoperatorContext):
        pass


    # Enter a parse tree produced by pascalParser#term.
    def enterTerm(self, ctx:pascalParser.TermContext):
        pass

    # Exit a parse tree produced by pascalParser#term.
    def exitTerm(self, ctx:pascalParser.TermContext):
        pass


    # Enter a parse tree produced by pascalParser#multiplicativeoperator.
    def enterMultiplicativeoperator(self, ctx:pascalParser.MultiplicativeoperatorContext):
        pass

    # Exit a parse tree produced by pascalParser#multiplicativeoperator.
    def exitMultiplicativeoperator(self, ctx:pascalParser.MultiplicativeoperatorContext):
        pass


    # Enter a parse tree produced by pascalParser#signedFactor.
    def enterSignedFactor(self, ctx:pascalParser.SignedFactorContext):
        pass

    # Exit a parse tree produced by pascalParser#signedFactor.
    def exitSignedFactor(self, ctx:pascalParser.SignedFactorContext):
        pass


    # Enter a parse tree produced by pascalParser#factor.
    def enterFactor(self, ctx:pascalParser.FactorContext):
        pass

    # Exit a parse tree produced by pascalParser#factor.
    def exitFactor(self, ctx:pascalParser.FactorContext):
        pass


    # Enter a parse tree produced by pascalParser#unsignedConstant.
    def enterUnsignedConstant(self, ctx:pascalParser.UnsignedConstantContext):
        pass

    # Exit a parse tree produced by pascalParser#unsignedConstant.
    def exitUnsignedConstant(self, ctx:pascalParser.UnsignedConstantContext):
        pass


    # Enter a parse tree produced by pascalParser#functionDesignator.
    def enterFunctionDesignator(self, ctx:pascalParser.FunctionDesignatorContext):
        pass

    # Exit a parse tree produced by pascalParser#functionDesignator.
    def exitFunctionDesignator(self, ctx:pascalParser.FunctionDesignatorContext):
        pass


    # Enter a parse tree produced by pascalParser#parameterList.
    def enterParameterList(self, ctx:pascalParser.ParameterListContext):
        pass

    # Exit a parse tree produced by pascalParser#parameterList.
    def exitParameterList(self, ctx:pascalParser.ParameterListContext):
        pass


    # Enter a parse tree produced by pascalParser#set_.
    def enterSet_(self, ctx:pascalParser.Set_Context):
        pass

    # Exit a parse tree produced by pascalParser#set_.
    def exitSet_(self, ctx:pascalParser.Set_Context):
        pass


    # Enter a parse tree produced by pascalParser#elementList.
    def enterElementList(self, ctx:pascalParser.ElementListContext):
        pass

    # Exit a parse tree produced by pascalParser#elementList.
    def exitElementList(self, ctx:pascalParser.ElementListContext):
        pass


    # Enter a parse tree produced by pascalParser#element.
    def enterElement(self, ctx:pascalParser.ElementContext):
        pass

    # Exit a parse tree produced by pascalParser#element.
    def exitElement(self, ctx:pascalParser.ElementContext):
        pass


    # Enter a parse tree produced by pascalParser#procedureStatement.
    def enterProcedureStatement(self, ctx:pascalParser.ProcedureStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureStatement.
    def exitProcedureStatement(self, ctx:pascalParser.ProcedureStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#actualParameter.
    def enterActualParameter(self, ctx:pascalParser.ActualParameterContext):
        pass

    # Exit a parse tree produced by pascalParser#actualParameter.
    def exitActualParameter(self, ctx:pascalParser.ActualParameterContext):
        pass


    # Enter a parse tree produced by pascalParser#parameterwidth.
    def enterParameterwidth(self, ctx:pascalParser.ParameterwidthContext):
        pass

    # Exit a parse tree produced by pascalParser#parameterwidth.
    def exitParameterwidth(self, ctx:pascalParser.ParameterwidthContext):
        pass


    # Enter a parse tree produced by pascalParser#gotoStatement.
    def enterGotoStatement(self, ctx:pascalParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#gotoStatement.
    def exitGotoStatement(self, ctx:pascalParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#emptyStatement.
    def enterEmptyStatement(self, ctx:pascalParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#emptyStatement.
    def exitEmptyStatement(self, ctx:pascalParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#empty_.
    def enterEmpty_(self, ctx:pascalParser.Empty_Context):
        pass

    # Exit a parse tree produced by pascalParser#empty_.
    def exitEmpty_(self, ctx:pascalParser.Empty_Context):
        pass


    # Enter a parse tree produced by pascalParser#structuredStatement.
    def enterStructuredStatement(self, ctx:pascalParser.StructuredStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#structuredStatement.
    def exitStructuredStatement(self, ctx:pascalParser.StructuredStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#compoundStatement.
    def enterCompoundStatement(self, ctx:pascalParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#compoundStatement.
    def exitCompoundStatement(self, ctx:pascalParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#statements.
    def enterStatements(self, ctx:pascalParser.StatementsContext):
        pass

    # Exit a parse tree produced by pascalParser#statements.
    def exitStatements(self, ctx:pascalParser.StatementsContext):
        pass


    # Enter a parse tree produced by pascalParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:pascalParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:pascalParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#ifStatement.
    def enterIfStatement(self, ctx:pascalParser.IfStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#ifStatement.
    def exitIfStatement(self, ctx:pascalParser.IfStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#caseStatement.
    def enterCaseStatement(self, ctx:pascalParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#caseStatement.
    def exitCaseStatement(self, ctx:pascalParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#caseListElement.
    def enterCaseListElement(self, ctx:pascalParser.CaseListElementContext):
        pass

    # Exit a parse tree produced by pascalParser#caseListElement.
    def exitCaseListElement(self, ctx:pascalParser.CaseListElementContext):
        pass


    # Enter a parse tree produced by pascalParser#repetetiveStatement.
    def enterRepetetiveStatement(self, ctx:pascalParser.RepetetiveStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#repetetiveStatement.
    def exitRepetetiveStatement(self, ctx:pascalParser.RepetetiveStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#whileStatement.
    def enterWhileStatement(self, ctx:pascalParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#whileStatement.
    def exitWhileStatement(self, ctx:pascalParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#repeatStatement.
    def enterRepeatStatement(self, ctx:pascalParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#repeatStatement.
    def exitRepeatStatement(self, ctx:pascalParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#forStatement.
    def enterForStatement(self, ctx:pascalParser.ForStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#forStatement.
    def exitForStatement(self, ctx:pascalParser.ForStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#forList.
    def enterForList(self, ctx:pascalParser.ForListContext):
        pass

    # Exit a parse tree produced by pascalParser#forList.
    def exitForList(self, ctx:pascalParser.ForListContext):
        pass


    # Enter a parse tree produced by pascalParser#initialValue.
    def enterInitialValue(self, ctx:pascalParser.InitialValueContext):
        pass

    # Exit a parse tree produced by pascalParser#initialValue.
    def exitInitialValue(self, ctx:pascalParser.InitialValueContext):
        pass


    # Enter a parse tree produced by pascalParser#finalValue.
    def enterFinalValue(self, ctx:pascalParser.FinalValueContext):
        pass

    # Exit a parse tree produced by pascalParser#finalValue.
    def exitFinalValue(self, ctx:pascalParser.FinalValueContext):
        pass


    # Enter a parse tree produced by pascalParser#withStatement.
    def enterWithStatement(self, ctx:pascalParser.WithStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#withStatement.
    def exitWithStatement(self, ctx:pascalParser.WithStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#recordVariableList.
    def enterRecordVariableList(self, ctx:pascalParser.RecordVariableListContext):
        pass

    # Exit a parse tree produced by pascalParser#recordVariableList.
    def exitRecordVariableList(self, ctx:pascalParser.RecordVariableListContext):
        pass



del pascalParser