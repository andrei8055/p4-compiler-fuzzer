import random
from bool import bool
from error import error
from bit import bit
from int import int
from varbit import varbit
from common import common


class base_type(object):
	type = 'type_ref'
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

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 5)
		if rnd == 0:
			self.value = bool()
		elif rnd == 1:
			self.value = error()
		elif rnd == 2:
			self.value = bit(None)
		elif rnd == 3:
			self.value = bit()
			self.value.randomize()
		elif rnd == 4:
			self.value = int()
			self.value.randomize()
		elif rnd == 5:
			self.value = varbit()
			self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
