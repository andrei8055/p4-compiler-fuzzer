from l_values.l_value_dot_member import l_value_dot_member
from prefixed_non_type import prefixed_non_type
from l_values.l_value_expression import l_value_expression
from l_values.l_value_expression_expression import l_value_expression_expression


class l_value(object):
	type = 'l_value'
	value = None

	# lvalue
	# 	: prefixedNonTypeName
	# 	| lvalue '.' member
	# 	| lvalue '[' expression ']'
	# 	| lvalue'['expression':'expression']'

	def __init__(self):
		pass

	def prefixed_non_type(self, prefix, non_type):
		return prefixed_non_type(prefix, non_type)

	def dot_member(self, l_value, member):
		return l_value_dot_member(l_value, member)

	def expression(self, l_value, expression):
		return l_value_expression(l_value, expression)

	def expression_expression(self, l_value, expression_1, expression_2):
		return l_value_expression_expression(l_value, expression_1, expression_2)

