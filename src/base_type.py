from bool import bool
from error import error
from bit import bit
from int import int
from varbit import varbit
from randomizer import randomizer


class base_type(object):
	type = None
	types = ["BOOL", "ERROR", "BIT", "BITOFINTEGER", "INTOFINTEGER", "VARBITOFINTEGER"]
	# TODO: implement TYPE and ERROR and set probabilities higher than 0 for them
	probabilities = [2,2,2,2,1,1]
	value = None

	# baseType
	# : BOOL
	# | ERROR
	# | BIT
	# | BIT '<'INTEGER'>'
	# | INT '<'INTEGER'>'
	# | VARBIT'<'INTEGER'>'
	# ;

	def __init__(self, value=None):
		self.value = value

	def get_type(self):
		return self.types[self.type]

	def get_ref_type(self):
		return self.value.get_ref_type()

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = bool()
		elif self.type == 1:
			self.value = error()
		elif self.type == 2:
			self.value = bit(None)
		elif self.type == 3:
			self.value = bit()
			self.value.randomize()
		elif self.type == 4:
			self.value = int()
			self.value.randomize()
		elif self.type == 5:
			self.value = varbit()
			self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
