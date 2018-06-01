from dontcare_literal import dontcare_literal
from randomizer import randomizer


class type_arg(object):
	type = None
	types = ["DONTCARE", "typeRef"]
	probabilities = [50, 50]
	value = None

	# typeArg
	# : DONTCARE
	# | typeRef
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = dontcare_literal()
		elif self.type == 1:
			from type_ref import type_ref
			self.value = type_ref()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
