from common import common
from randomizer import randomizer


class error(object):
	name = 'error'
	identifier_list = []

	def __init__(self, identifier_list=None):
		self.identifier_list = identifier_list if identifier_list is not None else []

	def get_name(self):
		return self.name

	def get_ref_type(self):
		return "error"

	def get_type_decl(self):
		return self

	def get_identifier_list(self):
		return self.identifier_list

	def randomize(self):
		self.identifier_list = []  # todo randomize

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = self.get_name()
		identifier_list = self.get_identifier_list()
		for x in range(0, len(identifier_list)):
			code += code + str(identifier_list[x])
			if x < len(identifier_list) - 1:
				code = code + ', '
		return code

	def generate_code_ref(self):
		return 'error'

	def generate_literal(self):
		rnd = randomizer.randint(0, 5)
		code = "error."
		if rnd == 0:
			code += "NoError"
		if rnd == 1:
			code += "PacketTooShort"
		if rnd == 2:
			code += "NoMatch"
		if rnd == 3:
			code += "StackOutOfBounds"
		if rnd == 4:
			code += "HeaderTooShort"
		if rnd == 5:
			code += "ParserTimeout"
		return code