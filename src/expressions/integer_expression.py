class integer_expression(object):
	type = 'integer_expression'
	value = 0

	def __init__(self, value):
		self.name = value

	def generate_code(self):
		return self.value
