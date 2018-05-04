import random
from function_prototype import function_prototype
from parameter_list import parameter_list
from common import common


class method_prototype(object):
	type = 'method_prototype'
	value = None

	# methodPrototype
	# : functionPrototype ';'
	# | TYPE '(' parameterList')' ';'
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.value = function_prototype()
		elif rnd == 1:
			self.value = parameter_list()
		self.value.randomize()

	def generate_code(self):
		if type(self.value).__name__ == 'function_prototype':
			return self.value.generate_code() + ';'
		elif type(self.value).__name__ == 'parameter_list':
			return 'type (' + self.value.generate_code() + ');'
		else:
			return 'ERROR in method_prototype - unknown type'
