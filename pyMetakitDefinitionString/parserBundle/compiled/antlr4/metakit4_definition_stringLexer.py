# Generated from grammar.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
	with StringIO() as buf:
		buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
		buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
		buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3")
		buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
		buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\2\2\16\3\3")
		buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
		buf.write("\3\2\t\22\2\62;CCEEGGIJLNPTV\\aacceeggijlnptv|\4\2\62")
		buf.write(";aa\t\2CCEEGGIJLNPTV\\\t\2cceeggijlnptv|\16\2DDFFHHKK")
		buf.write("OOUUddffhhkkoouu\b\2DDFFHHKKOOUU\b\2ddffhhkkoouu\2\62")
		buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
		buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
		buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2")
		buf.write("\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2")
		buf.write("\r%\3\2\2\2\17'\3\2\2\2\21)\3\2\2\2\23+\3\2\2\2\25-\3")
		buf.write("\2\2\2\27/\3\2\2\2\31\61\3\2\2\2\33\34\7]\2\2\34\4\3\2")
		buf.write("\2\2\35\36\7_\2\2\36\6\3\2\2\2\37 \7<\2\2 \b\3\2\2\2!")
		buf.write('"\7.\2\2"\n\3\2\2\2#$\7`\2\2$\f\3\2\2\2%&\t\2\2\2&\16')
		buf.write("\3\2\2\2'(\t\3\2\2(\20\3\2\2\2)*\t\4\2\2*\22\3\2\2\2")
		buf.write("+,\t\5\2\2,\24\3\2\2\2-.\t\6\2\2.\26\3\2\2\2/\60\t\7\2")
		buf.write("\2\60\30\3\2\2\2\61\62\t\b\2\2\62\32\3\2\2\2\3\2\2")
		return buf.getvalue()


class metakit4_definition_stringLexer(Lexer):

	atn = ATNDeserializer().deserialize(serializedATN())

	decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

	channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

	modeNames = ["DEFAULT_MODE"]

	literalNames = ["<INVALID>", "'['", "']'", "':'", "','", "'^'"]

	symbolicNames = ["<INVALID>", "SubFieldsStart", "SubFieldsEnd", "Colon", "OptionsSeparator", "IndirectMarker", "OtherWordChars", "OtherWordCharsOther", "OtherWordCharsUpper", "OtherWordCharsLower", "TypeSpecifier", "TypeSpecifierUpper", "TypeSpecifierLower"]

	ruleNames = ["SubFieldsStart", "SubFieldsEnd", "Colon", "OptionsSeparator", "IndirectMarker", "OtherWordChars", "OtherWordCharsOther", "OtherWordCharsUpper", "OtherWordCharsLower", "TypeSpecifier", "TypeSpecifierUpper", "TypeSpecifierLower"]

	grammarFileName = "grammar.g4"

	def __init__(self, input=None, output: TextIO = sys.stdout):
		super().__init__(input, output)
		self.checkVersion("4.8")
		self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
		self._actions = None
		self._predicates = None
