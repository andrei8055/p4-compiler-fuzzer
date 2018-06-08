from simple_keyset_expression import simple_keyset_expression
from simple_expression_list import simple_expression_list
from common import common


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
		common.usedRandomize()
		self.simple_keyset_expression = simple_keyset_expression()
		self.simple_keyset_expression.randomize()
		self.simple_expression_list = simple_expression_list()
		self.simple_expression_list.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return '(' + self.simple_keyset_expression.generate_code() + ', ' + self.simple_expression_list.generate_code() + ') '
