import random
from common import common

class identifier(object):
	type = 'identifier'
	value = ''
	min_identifier_length = 1
	max_identifier_length = 50

	def __init__(self, value=""):
		self.value = value

	def randomize(self):
		rnd = random.randint(0, 4)
		if rnd == 0:
			self.value = common.get_random_string(random.randint(self.min_identifier_length, self.max_identifier_length), False)

	def generate_code(self):
		return self.value
