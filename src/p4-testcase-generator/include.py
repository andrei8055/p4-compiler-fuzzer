from common import common
from randomizer import randomizer


class include(object):
	name = ''

	name_min_length = 1
	name_max_length = 50

	def __init__(self, name=''):
		self.name = name

	def randomize(self):
		common.get_random_string(randomizer.randint(self.name_min_length, self.name_max_length), False)

	def generate_code(self):
		common.usedCodeGenerator(self)
		return '#include' + '<' + self.name + '>'
