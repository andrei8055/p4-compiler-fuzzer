from common import common
from base_type_generator import base_type_generator


class variable(object):
	base_type_generator = base_type_generator()

	value = None
	type = None
	name = ''

	max_name_length = 50

	def __init__(self, name='', type=None, value=None):
		self.name = name
		self.value = value
		self.type = type

	def get_value(self):
		return self.value

	def get_type(self):
		return self.type

	def get_name(self):
		return self.name

	def randomize(self):
		common.usedRandomize()
		self.name = common.get_random_string(self.max_name_length, False)
		self.type = self.base_type_generator.generate_random(['bit', 'varbit', 'int'])
		self.value = 1  # todo generate random value based on type

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.type.generate_code() + ' ' + self.name + ' = ' + str(self.value) + ';'