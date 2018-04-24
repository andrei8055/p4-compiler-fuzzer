from name import name


class member(object):
	type = 'member'
	value = None

	# member
	# : name
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.value = name()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()

