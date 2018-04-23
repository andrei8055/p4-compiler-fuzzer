class method_call_statement(object):
	type = 'method_call_statement'
	l_value = None
	argument_list = None

	def __init__(self, l_value, argument_list=[]):
		self.l_value = l_value
		self.argument_list = argument_list

	def generate_code(self):
		code = ''
		code += self.l_value.generate_code() + '('
		parameters = self.argument_list
		for x in range(0, len(parameters)):
			code = code + str(parameters[x].generate_code())
			if x < len(parameters) - 1:
				code = code + ', '
		code += ')'
		return code
