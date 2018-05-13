from type_name import type_name
from argument_list import argument_list


class direct_application(object):
	type = 'direct_application'
	type_name = None
	argument_list = None

	# directApplication
	# : typeName '.' APPLY '(' argumentList ')' ';'

	def __init__(self, type_name=None, argument_list=None):
		self.type_name = type_name
		self.argument_list = argument_list

	def randomize(self):
		self.type_name = type_name()
		self.type_name.randomize()
		if self.type_name.prefixed_type is not None:
			self.argument_list = argument_list()
			self.argument_list.randomize()
		else:
			self.type_name = None

	def generate_code(self):
		return self.type_name.generate_code() + '.apply(' + self.argument_list.generate_code() + ');'

