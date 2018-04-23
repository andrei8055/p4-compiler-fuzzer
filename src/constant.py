from common import common
from base_type_generator import base_type_generator
from literal import literal

class constant(object):
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
		self.name = common.get_random_string(self.max_name_length, False)
		#self.type = self.base_type_generator.generate_random(['bit', 'varbit', 'int'])
		self.type = self.base_type_generator.generate_random(['int']) #  todo change to ['bit', 'varbit', 'int'] when literals are correctly generated
		self.value = literal.get(self.type)

	def generate_code(self):
		return 'const' + ' ' + self.type.generate_code() + ' ' + self.name + ' = ' + str(self.value) + ';'