from type_ref import type_ref
from void import void
from non_type_name import non_type_name
from randomizer import randomizer


class type_or_void(object):
	type = 'type_or_void'
	value = None

	# typeOrVoid
	# : typeRef
	# | VOID
	# | nonTypeName // may be a type variable
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = randomizer.randint(0, 5)
		if rnd == 0:
			self.value = type_ref()
		elif rnd == 1:
			self.value = void()
		elif rnd == 2:
			self.value = non_type_name(None)
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()