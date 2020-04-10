__all__ = ("parse",)

from pathlib import Path
from UniGrammarRuntime.ParserBundle import ParserBundle

thisFile = Path(__file__).absolute()
thisDir = thisFile.parent
bundleDir = thisDir / "parserBundle"

bundle = ParserBundle(bundleDir)

grammar = bundle.grammars["metakit4_definition_string"]
wrapper = grammar.getWrapper("antlr4")


parse = wrapper
