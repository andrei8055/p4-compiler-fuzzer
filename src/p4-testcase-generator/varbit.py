from randomizer import randomizer


class varbit(object):
	name = 'varbit'
	size = None

	min_size = 1
	max_size = 1000

	def __init__(self, size=1):
		self.name = 'varbit'
		self.size = size

	def get_ref_type(self):
		return "varbit"

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def randomize(self):
		self.size = randomizer.randint(self.min_size, self.max_size)

	def generate_code(self):
		return self.name + '<' + str(self.size) + '>'

	def generate_code_ref(self):
		return self.name + '<' + str(self.size) + '>'

