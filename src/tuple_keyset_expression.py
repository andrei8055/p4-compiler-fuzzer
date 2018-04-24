from keyset_expression import keyset_expression
from name import name

class tuple_keyset_expression(object):
	type = 'tuple_keyset_expression'
	simple_keyset_expression = None
	simple_expression_list = None

	# tupleKeysetExpression
	# : '(' simpleKeysetExpression ',' simpleExpressionList')'
	# ;

	def __init__(self, simple_keyset_expression=None, simple_expression_list=None):
		self.simple_keyset_expression = simple_keyset_expression
		self.simple_expression_list = simple_expression_list

	def randomize(self):
		self.simple_keyset_expression = simple_keyset_expression()
		self.simple_keyset_expression.randomize()
		self.simple_expression_list = simple_expression_list()
		self.simple_expression_list.randomize()

	def generate_code(self):
		return '(' + self.simple_keyset_expression.generate_code() + ', ' + self.simple_expression_list.generate_code() + ') '
