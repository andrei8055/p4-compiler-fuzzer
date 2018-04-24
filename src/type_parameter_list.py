from non_type import non_type
import random


class type_parameter_list(object):
	type = 'type_parameter_list'
	parameter_list = []
	min_list_size = 1
	max_list_size = 50

	# typeParameterList
	# : nonTypeName
	# | typeParameterList ','nonTypeName
	# ;

	def __init__(self, parameter_list=[]):
		self.parameter_list = parameter_list

	def randomize(self):
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_non_type = non_type()
			_non_type.randomize()
			self.parameter_list.append(_non_type)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.parameter_list)):
			code += self.parameter_list[x].generate_code()
			if x < len(self.parameter_list) - 1:
				code = code + ', '
		return code

