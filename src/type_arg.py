from type_ref import type_ref
from dontcare_literal import dontcare_literal
from non_type import non_type
import random

class type_arg(object):
	type = 'type_arg'
	value = None

	# typeArg
	# : DONTCARE
	# | typeRef
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.value = dontcare_literal()
		elif rnd == 1:
			self.value = type_ref()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
