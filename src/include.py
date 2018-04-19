from common import common

class include(object):
	name = ''

	name_min_length = 1
	name_max_length = 50
	common = common()

	def __init__(self, name=''):
		self.name = name

	def randomize(self):
		self.common.get_random_string(random.randint(self.name_min_length, self.name_max_length), False)

	def generate_code(self):
		return '#include' + '<' + self.name + '>'
