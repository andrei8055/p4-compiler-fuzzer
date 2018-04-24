from lvalue import lvalue
from expression import expression


class assignment_statement(object):
	type = 'assignment_declaration'
	lvalue = None
	expression = None

	# | lvalue '=' expression ';'

	def __init__(self, lvalue=None, expression=None):
		self.lvalue = lvalue
		self.expression = expression

	def randomize(self):
		self.lvalue = lvalue()
		self.lvalue.randomize()
		self.expression = expression()
		self.expression.randomize()

	def generate_code(self):
		return self.lvalue.generate_code() + ' = ' + self.expression.generate_code() + ';'

