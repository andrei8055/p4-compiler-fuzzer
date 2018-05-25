from dot_prefix import dot_prefix
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

	def get_ref_type(self):
		return self.value[self.value.keys()[0]]["type"]

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			available_types = scope.get_available_types()
			if len(available_types):
				rnd = randomizer.randint(0, len(available_types)-1)
				self.value = {available_types.keys()[rnd]: available_types[available_types.keys()[rnd]]}
		elif self.type == 1:
			self.prefix = dot_prefix()
			# TODO:
			self.value = None

	def generate_code(self):
		if self.prefix is not None:
			return self.prefix.generate_code() + self.value.keys()[0]
		else:
			return self.value.keys()[0]
