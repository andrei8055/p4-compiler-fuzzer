import random
from dot_prefix import dot_prefix
from common import common
from randomizer import randomizer
from scope import scope


class prefixed_type(object):
	type = None
	types = ["type", "dotPrefixType"]
	# TODO: implement dotPrefixType and set probability higher than 0 for it
	probabilities = [10,0]
	prefix = None
	value = None

	# prefixedType
	# : TYPE
	# | dotPrefix TYPE
	# ;

	def __init__(self, prefix=None, value=None):
		self.prefix = prefix
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			avaiable_types = scope.get_available_types()
			if len(avaiable_types):
				rnd = randomizer.randint(0, len(avaiable_types))
				self.value = avaiable_types[rnd]
		elif self.type == 1:
			self.prefix = dot_prefix()
			# TODO:
			self.value = None

	def generate_code(self):
		if self.prefix is not None:
			return self.prefix.generate_code() + self.value
		else:
			return self.value
