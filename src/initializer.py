from expression import expression


class initializer(object):
	type = 'initializer'
	value = None

	# initializer
	# : expression
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.value = expression()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()

