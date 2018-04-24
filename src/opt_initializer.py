from initializer import initializer
import random

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
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.initializer = initializer()
			self.initializer.randomize()
		else:
			self.initializer = None

	def generate_code(self):
		if self.initializer is not None:
			return '=' + self.initializer.generate_code()
		else:
			return ''
