from expression import expression
from statement import statement
from common import common


class conditional_statement(object):
	type = 'conditional_statement'
	expression = None
	if_statement = None
	else_statement = None

	# conditionalStatement
	# : IF '('expression ')' statement
	# | IF '('expression ')' statement ELSE statement
	# ;

	def __init__(self, expression=None, if_statement=None, else_statement=None):
		self.expression = expression
		self.if_statement = if_statement
		self.else_statement = else_statement

	def randomize(self):
		common.usedRandomize()
		self.expression = expression()
		self.expression.randomize()
		self.if_statement = statement()
		self.if_statement.randomize()
		self.else_statement = statement()
		self.else_statement.randomize()

	def generate_code(self):
		code = 'if (' + self.expression.generate_code() + ')' + self.if_statement.generate_code() + ' '
		if self.else_statement is not None:
			code += ' else ' + self.if_statement.else_statement() + ' '
		return code

