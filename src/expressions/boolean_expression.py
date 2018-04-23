class boolean_expression(object):
	type = 'boolean_expression'
	value = 'false'

	def __init__(self, value):
		if value in ['true', 'false']:
			self.value = value
		else:
			self.value = 'false'

	def generate_code(self):
		return self.value
