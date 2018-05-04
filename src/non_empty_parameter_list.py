from parameter import parameter
import random
from common import common


class non_empty_parameter_list(object):
	type = 'non_empty_parameter_list'
	parameter_list = []
	min_list_size = 1
	max_list_size = 5

	def __init__(self, parameter_list=[]):
		self.parameter_list = parameter_list

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_parameter = parameter()
			_parameter.randomize()
			self.parameter_list.append(_parameter)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.parameter_list)):
			code = code + self.parameter_list[x].generate_code()
			if x < len(self.parameter_list) - 1:
				code = code + ', '
		return code
