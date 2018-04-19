class varbit(object):
	name = 'varbit'
	size = None

	def __init__(self, size=0):
		self.name = 'varbit'
		self.size = size

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def generate_code(self):
		return self.name + '<' + str(self.size) + '>'