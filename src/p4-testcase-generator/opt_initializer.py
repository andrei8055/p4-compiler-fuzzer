from initializer import initializer
from randomizer import randomizer
from common import common


class opt_initializer(object):
	type = 'opt_initializer'
	initializer = None

	# optInitializer
	# : / *empty * /
	# | '=' initializer
	# ;

	def __init__(self, initializer=None):
		self.initializer = initializer

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.initializer = initializer()
			self.initializer.randomize()
		else:
			self.initializer = None

	def generate_code(self):
		common.usedCodeGenerator(self)
		if self.initializer is not None:
			return '=' + self.initializer.generate_code()
		else:
			return ''
