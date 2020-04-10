import typing
from UniGrammarRuntime.IWrapper import IWrapper, IParseResult


class view(IParseResult):
	__slots__ = "name", "bodyF"

	def __init__(self):
		self.name = None
		self.bodyF = None


class scalar(IParseResult):
	__slots__ = "name", "typeF"

	def __init__(self):
		self.name = None
		self.typeF = None


class subFieldsParser(IWrapper):
	__slots__ = ()

	def process_delimited_scalarOrView_(self, parsed) -> typing.Iterable[typing.Union[scalar, view]]:
		yield parsed.first_subField
		for f in self.backend.iterateCollection(parsed.rest_subFields_with_del):
			yield f.rest_subField

	def process_delimited_scalarOrView(self, parsed):
		return [self.process_scalarOrView(f) for f in self.process_delimited_scalarOrView_(parsed)]

	def process_scalarOrView(self, parsed) -> typing.Union[scalar, view]:
		scalarF = getattr(parsed, "scalarF", None)
		if scalarF is not None:
			return self.process_scalar(scalarF)
		viewF = getattr(parsed, "viewF", None)
		if viewF is not None:
			return self.process_view(viewF)
		raise TypeError(dir(parsed))

	def process_view(self, parsed) -> view:
		rec = view()
		rec.name = self.backend.getSubTreeText(parsed.name)
		rec.bodyF = self.process_body(parsed.bodyF)
		return rec

	def process_scalar(self, parsed) -> scalar:
		rec = scalar()
		rec.name = self.backend.getSubTreeText(parsed.name)
		rec.typeF = self.backend.terminalNodeToStr(parsed.typeF)
		return rec

	def process_body(self, parsed) -> typing.Union[typing.Iterable[typing.Union[scalar, view]], str]:
		subFieldsF = getattr(parsed, "subFieldsF", None)
		if subFieldsF is not None:
			return self.process_delimited_scalarOrView(subFieldsF)
		selfF = getattr(parsed, "selfF", None)
		if selfF is not None:
			return self.backend.terminalNodeToStr(selfF)
		raise TypeError(dir(parsed))

	__MAIN_PRODUCTION__ = process_delimited_scalarOrView


__MAIN_PARSER__ = subFieldsParser
