import random
from in_literal import in_literal
from inout_literal import inout_literal
from out_literal import out_literal
from empty_literal import empty_literal
from common import common

class direction(object):
	type = 'direction'
	value = None

	# direction
	# : IN
	# | OUT
	# | INOUT
	# | / *empty * /
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 3)
		if rnd == 0:
			self.value = in_literal()
		elif rnd == 1:
			self.value = inout_literal()
		elif rnd == 2:
			self.value = out_literal()
		elif rnd == 3:
			self.value = empty_literal()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
