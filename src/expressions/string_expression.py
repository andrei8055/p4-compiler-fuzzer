class string_expression(object):
	type = 'string_expression'
	value = ''

	def __init__(self, value):
		self.value = value
			
	def generate_code(self):
		return self.value
