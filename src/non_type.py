import random
from identifier import identifier
from apply_literal import apply_literal
from key_literal import key_literal
from actions_literal import actions_literal
from state_literal import state_literal

class non_type(object):
	type = 'non_type'
	value = None

	# nonTypeName
	# : IDENTIFIER
	# | APPLY
	# | KEY
	# | ACTIONS
	# | STATE
	# ;

	def __init__(self, name=""):
		self.name = name

	def randomize(self):
		rnd = random.randint(0, 4)
		if rnd == 0:
			self.value = identifier()
		elif rnd == 1:
			self.value = apply_literal()
		elif rnd == 2:
			self.value = key_literal()
		elif rnd == 3:
			self.value = actions_literal()
		elif rnd == 4:
			self.value = state_literal()
			
		self.value.randomize()


	def generate_code(self):
		return self.value
