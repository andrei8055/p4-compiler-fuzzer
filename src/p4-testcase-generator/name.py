from non_type_name import non_type_name
from type_literal import type_literal
from error_literal import error_literal
from randomizer import randomizer
from common import common


class name(object):
	type = None
	types = ["nonTypeName", "TYPE", "ERROR"]
	probabilities = [100, 0, 0]
	value = None

	# name
	# : nonTypeName
	# | TYPE
	# | ERROR
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = non_type_name()
		elif self.type == 1:
			self.value = type_literal()
		elif self.type == 2:
			self.value = error_literal()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
