from bool import bool
from error import error
from bit import bit
from int import int
from varbit import varbit
from randomizer import randomizer
from common import common


class base_type(object):
	type = None
	types = ["BOOL", "ERROR", "BIT", "BITOFINTEGER", "INTOFINTEGER", "VARBITOFINTEGER"]
	probabilities = [20,0,20,20,20,10]
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

	def get_type_decl(self):
		return self.value.get_type_decl()

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
		common.usedCodeGenerator(self)
		return self.value.generate_code()

	def generate_literal(self):
		return self.value.generate_literal()