import random


class bit(object):
	name = 'bit'
	size = None

	min_size = 1
	max_size = 100000

	def __init__(self, size=0):
		self.name = 'bit'
		self.size = size

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def randomize(self):
		self.size = random.randint(self.min_size, self.max_size)

	def generate_code(self):
		if self.size is None:
			return self.name
		else:
			return self.name + '<' + str(self.size) + '>'

	def generate_code_ref(self):
		if self.size is None:
			return self.name
		else:
			return self.name + '<' + str(self.size) + '>'
