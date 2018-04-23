import random
from non_type import non_type

class prefixed_non_type(object):
	type = 'prefixed_non_type'
	prefix = False
	non_type = None

	def __init__(self, prefix=False, non_type=None):
		self.prefix = prefix
		self.non_type = non_type

	def randomize(self):
		self.prefix = random.choice([True, False])
		self.non_type = non_type()
		self.non_type.randomize()

	def generate_code(self):
		code = ''
		if self.prefix:
			code += '.'
		code += self.non_type.generate_code()
		return code
