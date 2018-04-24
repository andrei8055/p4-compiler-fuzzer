from argument import argument
import random


class non_empty_arg_list(object):
	type = 'non_empty_arg_list'
	argmument_list = []
	min_list_size = 1
	max_list_size = 50

	def __init__(self, argmument_list=[]):
		self.argmument_list = argmument_list

	def randomize(self):
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