from common import common
from randomizer import randomizer


class identifier(object):
	type = 'identifier'
	value = ''
	min_identifier_length = 1
	max_identifier_length = 50

	keywords = ["action", "const", "enum", "false", "in", "package", "select", "table", "typedef",
				"apply", "control", "error", "header", "inout", "parser", "state", "transition", "varbit",
				"bit", "default", "extern", "header_union", "int", "out", "struct", "true", "verify",
				"bool", "else", "exit", "if", "match_kind", "return", "switch", "tuple", "void"]

	def __init__(self, value=""):
		self.value = value

	def randomize(self):
		while True:
			self.value = common.get_random_string(randomizer.randint(self.min_identifier_length, self.max_identifier_length), False)
			if not self.filter():
				break

	def generate_code(self):
		return self.value

	def filter(self):
		if self.value in identifier.keywords:
			return True
		return False
