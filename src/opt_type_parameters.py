from type_parameter_list import type_parameter_list
import random


class opt_type_parameters(object):
	type = 'opt_type_parameters'
	type_parameter_list = None

	# optTypeParameters
	# : / *empty * /
	# | '<'typeParameterList'>'
	# ;

	def __init__(self, type_parameter_list=None):
		self.type_parameter_list = type_parameter_list

	def randomize(self):
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.type_parameter_list = None
		else:
			self.type_parameter_list = type_parameter_list()
			self.type_parameter_list.randomize()

	def generate_code(self):
		if self.type_parameter_list is not None:
			return '<' + self.type_parameter_list.generate_code() + '>'
		else:
			return ''
