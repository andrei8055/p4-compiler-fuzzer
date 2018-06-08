from randomizer import randomizer
from function_prototype import function_prototype
from parameter_list import parameter_list
from common import common


class method_prototype(object):
	type = None
	types = ["functionPrototype", "typeParameterList"]
	# TODO: include typeParameterList as well
	probabilities = [100,0]
	value = None

	# methodPrototype
	# : functionPrototype ';'
	# | TYPE '(' parameterList')' ';'
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = function_prototype()
		elif self.type == 1:
			self.value = parameter_list()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		if self.type == 0:
			return self.value.generate_code() + ';'
		elif self.type == 1:
			return 'type (' + self.value.generate_code() + ');'
