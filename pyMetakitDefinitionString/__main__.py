import sys

if __name__ == "__main__":
	from . import parse
	from pprint import pprint

	for el in sys.argv[1:]:
		pprint(parse(el))
