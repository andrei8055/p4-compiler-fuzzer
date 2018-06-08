from name import name
from common import common


class member(object):
	type = 'member'
	value = None

	# member
	# : name
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		self.value = name()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()

