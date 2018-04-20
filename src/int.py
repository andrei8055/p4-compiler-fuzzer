import random


class int(object):
	name = 'int'
	size = None

	min_size = 1
	max_size = 100000

	def get_name(self):
		return self.name

	def __init__(self, size=0):
		self.name = 'int'
		self.size = size

	def get_size(self):
		return self.size

	def randomize(self):
		self.size = random.randint(self.min_size, self.max_size)

	def generate_code(self):
		return self.name + '<' + str(self.size) + '>'

	def generate_code_ref(self):
		return self.name + '<' + str(self.size) + '>'
