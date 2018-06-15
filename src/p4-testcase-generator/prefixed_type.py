from dot_prefix import dot_prefix
from randomizer import randomizer
from scope import scope
from common import common


class prefixed_type(object):
	type = None
	types = ["type", "dotPrefixType"]
	# TODO: implement dotPrefixType and set probability higher than 0 for it
	probabilities = [100,0]
	prefix = None
	value = None
	specializations_refs = None

	# prefixedType
	# : TYPE
	# | dotPrefix TYPE
	# ;

	def __init__(self, prefix=None, value=None):
		self.prefix = prefix
		self.value = value
		self.specializations_refs = []


	def get_ref_type(self):
		return self.value[self.value.keys()[0]]["type"]

	def get_type_decl(self):
		return self.value[self.value.keys()[0]]["object"]

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			available_types = scope.get_available_types()
			from type_ref import type_ref
			if len(available_types):
				rnd = randomizer.randint(0, len(available_types)-1)
				rnd_key = available_types.keys()[rnd]
				specializations = available_types[rnd_key]["specializations"]
				self.value = {rnd_key: available_types[rnd_key]}
				for x in range(0, specializations):
					while True:
						_type_ref = type_ref()
						_type_ref.randomize()
						if not self.specialization_filter(_type_ref):
							break
					self.specializations_refs.append(_type_ref)
		elif self.type == 1:
			self.prefix = dot_prefix()
			# TODO:
			self.value = None

	def generate_code(self):
		common.usedCodeGenerator(self)
		if self.prefix is not None:
			return self.prefix.generate_code() + self.value.keys()[0]
		else:
			code = ""
			code += self.value.keys()[0]
			if len(self.specializations_refs) > 0:
				code += "<"
				for i, specialization_ref in enumerate(self.specializations_refs):
					code += specialization_ref.generate_code()
					if i < len(self.specializations_refs) - 1:
						code += ", "
				code += ">"
			return code

	def specialization_filter(self, specialization_ref):
		if specialization_ref.get_type() == 'specializedType':
			return True
		if specialization_ref.get_type() == 'headerStackType':
			return True
		return False