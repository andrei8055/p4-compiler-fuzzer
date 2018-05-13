from type_arg import type_arg
import random


class type_argument_list(object):
	type = 'type_argument_list'
	argument_list = []
	min_list_size = 1
	max_list_size = 5

	# typeArgumentList
	# : typeArg
	# | typeArgumentList ','typeArg
	# ;

	def __init__(self, argument_list=None):
		self.argument_list = argument_list if argument_list is not None else []

	def randomize(self):
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_arg_type = type_arg()
			_arg_type.randomize()
			self.argument_list.append(_arg_type)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.argument_list)):
			code += self.argument_list[x].generate_code()
			if x < len(self.argument_list) - 1:
				code = code + ', '
		return code

