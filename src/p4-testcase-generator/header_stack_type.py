from type_name import type_name
from expression import expression


class header_stack_type(object):
	type = 'header_stack_type'
	type_name = None
	expression = None

	# headerStackType
	# : typeName '[' expression']'
	# ;

	def __init__(self, type_name=None, expression=None):
		self.type_name = type_name
		self.expression = expression

	def get_ref_type(self):
		return "header_stack"

	def randomize(self):
		self.type_name = type_name()
		self.type_name.randomize()
		if self.type_name.prefixed_type is not None:
			self.expression = expression()
			self.expression.randomize()
		else:
			self.type_name = None

	def generate_code(self):
		return self.type_name.generate_code() + ' [' + self.expression.generate_code() + ']'
