class expression(object):
	value = ''
	type = ''

	def __init__(self, type, value):
		self.value = value
		self.type = type

	def get_value(self):
		return self.value

	def get_type(self):
		return self.type
