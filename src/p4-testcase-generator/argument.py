from expression import expression
from common import common


class argument(object):
	type = 'argument'
	value = None

	# argument
	# : expression
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		self.value = expression()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()

