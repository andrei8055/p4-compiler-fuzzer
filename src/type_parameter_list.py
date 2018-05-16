from non_type_name import non_type_name
from randomizer import randomizer


class type_parameter_list(object):
	type = 'type_parameter_list'
	parameter_list = []
	min_list_size = 1
	max_list_size = 5

	# typeParameterList
	# : nonTypeName
	# | typeParameterList ','nonTypeName
	# ;

	def __init__(self, parameter_list=None):
		self.parameter_list = parameter_list if parameter_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_non_type_name = non_type_name()
			_non_type_name.randomize()
			self.parameter_list.append(_non_type_name)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.parameter_list)):
			code += self.parameter_list[x].generate_code()
			if x < len(self.parameter_list) - 1:
				code = code + ', '
		return code

