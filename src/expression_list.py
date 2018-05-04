from expression import expression
import random
from common import common


class expression_list(object):
	type = 'expression_list'
	exp_list = []
	min_list_size = 0
	max_list_size = 5

	def __init__(self, exp_list=[]):
		self.exp_list = exp_list

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_expression = expression()
			_expression.randomize()
			self.exp_list.append(_expression)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.exp_list)):
			code = code + self.exp_list[x].generate_code()
			if x < len(self.exp_list) - 1:
				code = code + ', '
		return code
