from type_or_void import type_or_void
from name import name
from opt_type_parameters import opt_type_parameters
from parameter_list import parameter_list


class function_prototype(object):
	type = 'function_prototype'

	type_or_void = None
	name = None
	opt_type_parameters = None
	parameter_list = None

	# functionPrototype
	# : typeOrVoid name optTypeParameters '(' parameterList ')'
	# ;

	def __init__(self, type_or_void=None, name=None, opt_type_parameters=None, parameter_list=None):
		self.type_or_void = type_or_void
		self.name = name
		self.opt_type_parameters = opt_type_parameters
		self.parameter_list = parameter_list

	def randomize(self):
		self.type_or_void = type_or_void()
		self.type_or_void.randomize()
		self.name = name()
		self.name.randomize()
		self.opt_type_parameters = opt_type_parameters()
		self.opt_type_parameters.randomize()
		self.parameter_list = parameter_list()
		self.parameter_list.randomize()

	def generate_code(self):
		return self.type_or_void.generate_code() + ' ' + self.name.generate_code() + ' ' + self.opt_type_parameters.generate_code() + ' (' + self.parameter_list.generate_code() + ')'