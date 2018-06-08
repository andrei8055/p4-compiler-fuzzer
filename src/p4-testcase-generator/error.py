from common import common


class error(object):
	name = 'error'
	identifier_list = []

	def __init__(self, identifier_list=None):
		self.identifier_list = identifier_list if identifier_list is not None else []

	def get_name(self):
		return self.name

	def get_ref_type(self):
		return "error"

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
