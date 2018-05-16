from l_value import l_value
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
		self.lvalue = l_value()
		self.lvalue.randomize()
		self.expression = expression()
		self.expression.randomize()

	def generate_code(self):
		return self.lvalue.generate_code() + ' = ' + self.expression.generate_code() + ';'

