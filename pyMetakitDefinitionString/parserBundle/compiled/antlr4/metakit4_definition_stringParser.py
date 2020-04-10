# Generated from grammar.g4 by ANTLR 4.8
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
		buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
		buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
		buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\5\3\32\n\3\3")
		buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\5\6'\n\6\3")
		buf.write("\7\7\7*\n\7\f\7\16\7-\13\7\3\b\3\b\3\b\3\t\6\t\63\n\t")
		buf.write("\r\t\16\t\64\3\n\3\n\6\n9\n\n\r\n\16\n:\5\n=\n\n\3\n\2")
		buf.write("\2\13\2\4\6\b\n\f\16\20\22\2\2\2;\2\24\3\2\2\2\4\31\3")
		buf.write("\2\2\2\6\33\3\2\2\2\b \3\2\2\2\n&\3\2\2\2\f+\3\2\2\2\16")
		buf.write(".\3\2\2\2\20\62\3\2\2\2\22<\3\2\2\2\24\25\5\4\3\2\25\26")
		buf.write("\5\f\7\2\26\3\3\2\2\2\27\32\5\b\5\2\30\32\5\6\4\2\31\27")
		buf.write("\3\2\2\2\31\30\3\2\2\2\32\5\3\2\2\2\33\34\5\20\t\2\34")
		buf.write("\35\7\3\2\2\35\36\5\n\6\2\36\37\7\4\2\2\37\7\3\2\2\2 ")
		buf.write('!\5\20\t\2!"\7\5\2\2"#\7\f\2\2#\t\3\2\2\2$\'\5\2\2\2')
		buf.write("%'\7\7\2\2&$\3\2\2\2&%\3\2\2\2'\13\3\2\2\2(*\5\16\b")
		buf.write("\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\r\3\2\2\2")
		buf.write("-+\3\2\2\2./\7\6\2\2/\60\5\4\3\2\60\17\3\2\2\2\61\63\5")
		buf.write("\22\n\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65")
		buf.write("\3\2\2\2\65\21\3\2\2\2\66=\7\f\2\2\679\7\b\2\28\67\3\2")
		buf.write("\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<\66\3\2\2")
		buf.write("\2<8\3\2\2\2=\23\3\2\2\2\b\31&+\64:<")
		return buf.getvalue()


class metakit4_definition_stringParser(Parser):

	grammarFileName = "grammar.g4"

	atn = ATNDeserializer().deserialize(serializedATN())

	decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

	sharedContextCache = PredictionContextCache()

	literalNames = ["<INVALID>", "'['", "']'", "':'", "','", "'^'"]

	symbolicNames = ["<INVALID>", "SubFieldsStart", "SubFieldsEnd", "Colon", "OptionsSeparator", "IndirectMarker", "OtherWordChars", "OtherWordCharsOther", "OtherWordCharsUpper", "OtherWordCharsLower", "TypeSpecifier", "TypeSpecifierUpper", "TypeSpecifierLower"]

	RULE_subFields = 0
	RULE_scalarOrView = 1
	RULE_view = 2
	RULE_scalar = 3
	RULE_body = 4
	RULE_rest_subFields_with_delF = 5
	RULE_rest_subField_with_delF = 6
	RULE_word = 7
	RULE_wordPiece = 8

	ruleNames = ["subFields", "scalarOrView", "view", "scalar", "body", "rest_subFields_with_delF", "rest_subField_with_delF", "word", "wordPiece"]

	EOF = Token.EOF
	SubFieldsStart = 1
	SubFieldsEnd = 2
	Colon = 3
	OptionsSeparator = 4
	IndirectMarker = 5
	OtherWordChars = 6
	OtherWordCharsOther = 7
	OtherWordCharsUpper = 8
	OtherWordCharsLower = 9
	TypeSpecifier = 10
	TypeSpecifierUpper = 11
	TypeSpecifierLower = 12

	def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
		super().__init__(input, output)
		self.checkVersion("4.8")
		self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
		self._predicates = None

	class SubFieldsContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser
			self.first_subField = None  # ScalarOrViewContext
			self.rest_subFields_with_del = None  # Rest_subFields_with_delFContext

		def scalarOrView(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.ScalarOrViewContext, 0)

		def rest_subFields_with_delF(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.Rest_subFields_with_delFContext, 0)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_subFields

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterSubFields"):
				listener.enterSubFields(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitSubFields"):
				listener.exitSubFields(self)

	def subFields(self):

		localctx = metakit4_definition_stringParser.SubFieldsContext(self, self._ctx, self.state)
		self.enterRule(localctx, 0, self.RULE_subFields)
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 18
			localctx.first_subField = self.scalarOrView()
			self.state = 19
			localctx.rest_subFields_with_del = self.rest_subFields_with_delF()
		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class ScalarOrViewContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser
			self.scalarF = None  # ScalarContext
			self.viewF = None  # ViewContext

		def scalar(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.ScalarContext, 0)

		def view(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.ViewContext, 0)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_scalarOrView

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterScalarOrView"):
				listener.enterScalarOrView(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitScalarOrView"):
				listener.exitScalarOrView(self)

	def scalarOrView(self):

		localctx = metakit4_definition_stringParser.ScalarOrViewContext(self, self._ctx, self.state)
		self.enterRule(localctx, 2, self.RULE_scalarOrView)
		try:
			self.state = 23
			self._errHandler.sync(self)
			la_ = self._interp.adaptivePredict(self._input, 0, self._ctx)
			if la_ == 1:
				self.enterOuterAlt(localctx, 1)
				self.state = 21
				localctx.scalarF = self.scalar()
				pass

			elif la_ == 2:
				self.enterOuterAlt(localctx, 2)
				self.state = 22
				localctx.viewF = self.view()
				pass

		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class ViewContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser
			self.name = None  # WordContext
			self.bodyF = None  # BodyContext

		def SubFieldsStart(self):
			return self.getToken(metakit4_definition_stringParser.SubFieldsStart, 0)

		def SubFieldsEnd(self):
			return self.getToken(metakit4_definition_stringParser.SubFieldsEnd, 0)

		def word(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.WordContext, 0)

		def body(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.BodyContext, 0)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_view

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterView"):
				listener.enterView(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitView"):
				listener.exitView(self)

	def view(self):

		localctx = metakit4_definition_stringParser.ViewContext(self, self._ctx, self.state)
		self.enterRule(localctx, 4, self.RULE_view)
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 25
			localctx.name = self.word()
			self.state = 26
			self.match(metakit4_definition_stringParser.SubFieldsStart)
			self.state = 27
			localctx.bodyF = self.body()
			self.state = 28
			self.match(metakit4_definition_stringParser.SubFieldsEnd)
		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class ScalarContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser
			self.name = None  # WordContext
			self.typeF = None  # Token

		def Colon(self):
			return self.getToken(metakit4_definition_stringParser.Colon, 0)

		def word(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.WordContext, 0)

		def TypeSpecifier(self):
			return self.getToken(metakit4_definition_stringParser.TypeSpecifier, 0)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_scalar

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterScalar"):
				listener.enterScalar(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitScalar"):
				listener.exitScalar(self)

	def scalar(self):

		localctx = metakit4_definition_stringParser.ScalarContext(self, self._ctx, self.state)
		self.enterRule(localctx, 6, self.RULE_scalar)
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 30
			localctx.name = self.word()
			self.state = 31
			self.match(metakit4_definition_stringParser.Colon)
			self.state = 32
			localctx.typeF = self.match(metakit4_definition_stringParser.TypeSpecifier)
		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class BodyContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser
			self.subFieldsF = None  # SubFieldsContext
			self.selfF = None  # Token

		def subFields(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.SubFieldsContext, 0)

		def IndirectMarker(self):
			return self.getToken(metakit4_definition_stringParser.IndirectMarker, 0)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_body

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterBody"):
				listener.enterBody(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitBody"):
				listener.exitBody(self)

	def body(self):

		localctx = metakit4_definition_stringParser.BodyContext(self, self._ctx, self.state)
		self.enterRule(localctx, 8, self.RULE_body)
		try:
			self.state = 36
			self._errHandler.sync(self)
			token = self._input.LA(1)
			if token in [metakit4_definition_stringParser.OtherWordChars, metakit4_definition_stringParser.TypeSpecifier]:
				self.enterOuterAlt(localctx, 1)
				self.state = 34
				localctx.subFieldsF = self.subFields()
				pass
			elif token in [metakit4_definition_stringParser.IndirectMarker]:
				self.enterOuterAlt(localctx, 2)
				self.state = 35
				localctx.selfF = self.match(metakit4_definition_stringParser.IndirectMarker)
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

	class Rest_subFields_with_delFContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def rest_subField_with_delF(self, i: int = None):
			if i is None:
				return self.getTypedRuleContexts(metakit4_definition_stringParser.Rest_subField_with_delFContext)
			else:
				return self.getTypedRuleContext(metakit4_definition_stringParser.Rest_subField_with_delFContext, i)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_rest_subFields_with_delF

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterRest_subFields_with_delF"):
				listener.enterRest_subFields_with_delF(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitRest_subFields_with_delF"):
				listener.exitRest_subFields_with_delF(self)

	def rest_subFields_with_delF(self):

		localctx = metakit4_definition_stringParser.Rest_subFields_with_delFContext(self, self._ctx, self.state)
		self.enterRule(localctx, 10, self.RULE_rest_subFields_with_delF)
		self._la = 0  # Token type
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 41
			self._errHandler.sync(self)
			_la = self._input.LA(1)
			while _la == metakit4_definition_stringParser.OptionsSeparator:
				self.state = 38
				self.rest_subField_with_delF()
				self.state = 43
				self._errHandler.sync(self)
				_la = self._input.LA(1)

		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class Rest_subField_with_delFContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser
			self.rest_subField = None  # ScalarOrViewContext

		def OptionsSeparator(self):
			return self.getToken(metakit4_definition_stringParser.OptionsSeparator, 0)

		def scalarOrView(self):
			return self.getTypedRuleContext(metakit4_definition_stringParser.ScalarOrViewContext, 0)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_rest_subField_with_delF

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterRest_subField_with_delF"):
				listener.enterRest_subField_with_delF(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitRest_subField_with_delF"):
				listener.exitRest_subField_with_delF(self)

	def rest_subField_with_delF(self):

		localctx = metakit4_definition_stringParser.Rest_subField_with_delFContext(self, self._ctx, self.state)
		self.enterRule(localctx, 12, self.RULE_rest_subField_with_delF)
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 44
			self.match(metakit4_definition_stringParser.OptionsSeparator)
			self.state = 45
			localctx.rest_subField = self.scalarOrView()
		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class WordContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def wordPiece(self, i: int = None):
			if i is None:
				return self.getTypedRuleContexts(metakit4_definition_stringParser.WordPieceContext)
			else:
				return self.getTypedRuleContext(metakit4_definition_stringParser.WordPieceContext, i)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_word

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterWord"):
				listener.enterWord(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitWord"):
				listener.exitWord(self)

	def word(self):

		localctx = metakit4_definition_stringParser.WordContext(self, self._ctx, self.state)
		self.enterRule(localctx, 14, self.RULE_word)
		self._la = 0  # Token type
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 48
			self._errHandler.sync(self)
			_la = self._input.LA(1)
			while True:
				self.state = 47
				self.wordPiece()
				self.state = 50
				self._errHandler.sync(self)
				_la = self._input.LA(1)
				if not (_la == metakit4_definition_stringParser.OtherWordChars or _la == metakit4_definition_stringParser.TypeSpecifier):
					break

		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class WordPieceContext(ParserRuleContext):
		def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def TypeSpecifier(self):
			return self.getToken(metakit4_definition_stringParser.TypeSpecifier, 0)

		def OtherWordChars(self, i: int = None):
			if i is None:
				return self.getTokens(metakit4_definition_stringParser.OtherWordChars)
			else:
				return self.getToken(metakit4_definition_stringParser.OtherWordChars, i)

		def getRuleIndex(self):
			return metakit4_definition_stringParser.RULE_wordPiece

		def enterRule(self, listener: ParseTreeListener):
			if hasattr(listener, "enterWordPiece"):
				listener.enterWordPiece(self)

		def exitRule(self, listener: ParseTreeListener):
			if hasattr(listener, "exitWordPiece"):
				listener.exitWordPiece(self)

	def wordPiece(self):

		localctx = metakit4_definition_stringParser.WordPieceContext(self, self._ctx, self.state)
		self.enterRule(localctx, 16, self.RULE_wordPiece)
		try:
			self.state = 58
			self._errHandler.sync(self)
			token = self._input.LA(1)
			if token in [metakit4_definition_stringParser.TypeSpecifier]:
				self.enterOuterAlt(localctx, 1)
				self.state = 52
				self.match(metakit4_definition_stringParser.TypeSpecifier)
				pass
			elif token in [metakit4_definition_stringParser.OtherWordChars]:
				self.enterOuterAlt(localctx, 2)
				self.state = 54
				self._errHandler.sync(self)
				_alt = 1
				while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
					if _alt == 1:
						self.state = 53
						self.match(metakit4_definition_stringParser.OtherWordChars)

					else:
						raise NoViableAltException(self)
					self.state = 56
					self._errHandler.sync(self)
					_alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

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
