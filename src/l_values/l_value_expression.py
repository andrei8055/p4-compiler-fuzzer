class l_value_expression(object):
	type = 'l_value_expression'
	l_value = None
	expression = None
	# lvalue
	# 	: prefixedNonTypeName
	# 	| lvalue '.' member
	# 	| lvalue '[' expression ']'
	# 	| lvalue'['expression':'expression']'

	def __init__(self, l_value, expression):
		self.l_value = l_value
		self.expression = expression

	def generate_code(self):
		return self.l_value.generate_code() + '[' + self.expression.generate_code() + ']'
