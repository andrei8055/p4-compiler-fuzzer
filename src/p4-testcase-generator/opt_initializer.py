from initializer import initializer
from randomizer import randomizer
from common import common


class opt_initializer(object):
	type = None
	types = ["empty", "parameterList"]
	probabilities = [100, 0]
	initializer = None

	# optInitializer
	# : / *empty * /
	# | '=' initializer
	# ;

	def __init__(self, initializer=None):
		self.initializer = initializer

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.initializer = None
		else:
			self.initializer = initializer()
			self.initializer.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		if self.initializer is not None:
			return '= ' + self.initializer.generate_code()
		else:
			return ''
