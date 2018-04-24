import random
from non_type import non_type
from type_literal import type_literal
from error_literal import error_literal

class name(object):
	type = 'name'
	value = None

	# name
	# : nonTypeName
	# | TYPE
	# | ERROR
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = random.randint(0, 2)
		if rnd == 0:
			self.value = non_type()
		elif rnd == 1:
			self.value = type_literal()
		elif rnd == 2:
			self.value = error_literal()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
