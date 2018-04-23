class l_value_expression_expression(object):
	type = 'l_value_expression'
	l_value = None
	expression_1 = None
	expression_2 = None
	# lvalue
	# 	: prefixedNonTypeName
	# 	| lvalue '.' member
	# 	| lvalue '[' expression ']'
	# 	| lvalue'['expression':'expression']'

	def __init__(self, l_value, expression_1, expression_2):
		self.l_value = l_value
		self.expression_1 = expression_1
		self.expression_2 = expression_2

	def generate_code(self):
		return self.l_value.generate_code() + '[' + self.expression_1.generate_code() + ':' + self.expression_2.generate_code() + ']'
