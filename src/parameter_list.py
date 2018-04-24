from non_empty_parameter_list import non_empty_parameter_list
import random


class parameter_list(object):
	type = 'parameter_list'
	non_empty_parameter_list = None

	# parameterList
	# : / *empty * /
	# | nonEmptyParameterList
	# ;

	def __init__(self, non_empty_parameter_list=None):
		self.non_empty_parameter_list = non_empty_parameter_list

	def randomize(self):
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.non_empty_parameter_list = None
		else:
			self.non_empty_parameter_list = non_empty_parameter_list()
			self.non_empty_parameter_list.randomize()

	def generate_code(self):
		if self.non_empty_parameter_list is not None:
			return self.non_empty_parameter_list.generate_code()
		else:
			return ''

