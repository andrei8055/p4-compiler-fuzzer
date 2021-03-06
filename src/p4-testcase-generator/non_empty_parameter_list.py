from parameter import parameter
from randomizer import randomizer
from common import common


class non_empty_parameter_list(object):
	type = 'non_empty_parameter_list'
	parameter_list = []
	min_list_size = 1
	max_list_size = 5

	def __init__(self, parameter_list=None):
		self.parameter_list = parameter_list if parameter_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_parameter = parameter()
			_parameter.randomize()
			self.parameter_list.append(_parameter)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for x in range(0, len(self.parameter_list)):
			code = code + self.parameter_list[x].generate_code()
			if x < len(self.parameter_list) - 1:
				code = code + ', '
		return code
