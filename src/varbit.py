import random
from common import common


class varbit(object):
	name = 'varbit'
	size = None

	min_size = 0
	max_size = 1000

	def __init__(self, size=0):
		self.name = 'varbit'
		self.size = size

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def randomize(self):
		common.usedRandomize()
		self.size = random.randint(self.min_size, self.max_size)

	def generate_code(self):
		return self.name + '<' + str(self.size) + '>'

	def generate_code_ref(self):
		return self.name + '<' + str(self.size) + '>'

