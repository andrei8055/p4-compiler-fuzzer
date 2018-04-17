from common import common
from constant import constant
from base_type_generator import base_type_generator
from expression_generator import expression_generator
from base_type_generator import base_type_generator

class constant_generator(object):
	common = common()
	base_type_generator = base_type_generator()
	expression_generator = expression_generator()

	def generate(self, type, value):
		return constant(type, value)

	def generate_random(self):
		type = self.base_type_generator.generate_random_base_type(['error', 'bool', 'bit', 'varbit', 'int'])
		value = self.expression_generator.generate_random(type.get_type())
		print 'type = ' + self.base_type_generator.generate_code(type)
		print 'value = ' + value
		print 'done'
		return self.generate(type, value)

	def generate_code(self, constant):
		return 'const' + ' ' + self.base_type_generator.generate_code(constant.get_type()) + ' = ' + constant.get_value() + ';'
