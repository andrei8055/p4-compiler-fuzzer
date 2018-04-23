class assigment_statement(object):
	type = 'assigment_statement'
	l_value = None
	expression = None

	def __init__(self, l_value, expression):
		self.l_value = l_value
		self.expression = expression

	def generate_code(self):
		return self.l_value.generate_code() + ' = ' + self.expression.generate_code()
