from argument import argument
import random
from common import common


class non_empty_arg_list(object):
	type = 'non_empty_arg_list'
	argmument_list = []
	min_list_size = 1
	max_list_size = 5

	def __init__(self, argmument_list=None):
		self.argmument_list = argmument_list if argmument_list is not None else []

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_argument = argument()
			_argument.randomize()
			self.argmument_list.append(_argument)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.argmument_list)):
			code = code + self.argmument_list[x].generate_code()
			if x < len(self.argmument_list) - 1:
				code = code + ', '
		return code
