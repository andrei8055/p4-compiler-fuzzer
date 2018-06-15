from randomizer import randomizer
from common import common

class varbit(object):
	name = 'varbit'
	size = None

	min_size = 1
	max_size = 1000

	min_literal_val = 0
	max_literal_val = 1000

	def __init__(self, size=1):
		self.name = 'varbit'
		self.size = size

	def get_ref_type(self):
		return "varbit"

	def get_type_decl(self):
		return self

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def randomize(self):
		self.size = randomizer.randint(self.min_size, self.max_size)

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.name + '<' + str(self.size) + '>'

	def generate_code_ref(self):
		return self.name + '<' + str(self.size) + '>'

	def generate_literal(self):
		return str(randomizer.randint(self.min_literal_val, self.max_literal_val))