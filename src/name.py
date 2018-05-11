import random
from non_type_name import non_type_name
from type_literal import type_literal
from error_literal import error_literal
from common import common


class name(object):
	type = None
	types = ["type", "dotPrefixType"]
	# TODO: implement dotPrefixType and set probability higher than 0 for it
	probabilities = [10, 0]
	value = None

	# name
	# : nonTypeName
	# | TYPE
	# | ERROR
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 2)
		if rnd == 0:
			self.value = non_type_name()
		elif rnd == 1:
			self.value = type_literal()
		elif rnd == 2:
			self.value = error_literal()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
