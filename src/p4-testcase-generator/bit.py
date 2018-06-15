from randomizer import randomizer
from common import common


class bit(object):
	name = 'bit'
	size = None

	min_size = 1
	max_size = 100000

	min_literal_val = 0
	max_literal_val = 1000

	def __init__(self, size=0):
		self.name = 'bit'
		self.size = size

	def get_ref_type(self):
		return "bit"

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
		if self.size is None:
			return self.name
		else:
			return self.name + '<' + str(self.size) + '>'

	def generate_literal(self):
		return str(randomizer.randint(self.min_literal_val, self.max_literal_val))
