from randomizer import randomizer
from parameter_list import parameter_list
from common import common


class opt_constructor_parameters(object):
	type = None
	types = ["empty", "parameterList"]
	probabilities = [100, 0]

	parameter_list = None

	# optConstructorParameters
	# 	: / *empty * /
	# 	| '('parameterList ')'
	# 	;

	def __init__(self, parameter_list=None):
		self.parameter_list = parameter_list

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.parameter_list = None
		else:
			self.parameter_list = parameter_list()
			self.parameter_list.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		if self.parameter_list is not None:
			return '(' + self.parameter_list.generate_code() + ')'
		else:
			return ''
