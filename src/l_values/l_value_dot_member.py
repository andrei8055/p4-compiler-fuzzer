class l_value_dot_member(object):
	type = 'l_value_dot_member'
	l_value = None
	member = None
	# lvalue
	# 	: prefixedNonTypeName
	# 	| lvalue '.' member
	# 	| lvalue '[' expression ']'
	# 	| lvalue'['expression':'expression']'

	def __init__(self, l_value, member):
		self.l_value = l_value
		self.member = member

	def generate_code(self):
		return self.l_value.generate_code() + '.' + self.member.generate_code()
