from identifier import identifier
from apply_literal import apply_literal
from key_literal import key_literal
from actions_literal import actions_literal
from state_literal import state_literal
from randomizer import randomizer


class non_type_name(object):
	type = None
	types = ["IDENTIFIER", "APPLY", "KEY", "ACTIONS", "STATE"]
	# TODO: implement APPLY, KEY, ACTIONS, STATE and set probabilities higher than 0 for them
	probabilities = [10, 0, 0, 0, 0]
	value = None

	# nonTypeName
	# : IDENTIFIER
	# | APPLY
	# | KEY
	# | ACTIONS
	# | STATE
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = identifier()
		elif self.type == 1:
			self.value = apply_literal()
		elif self.type == 2:
			self.value = key_literal()
		elif self.type == 3:
			self.value = actions_literal()
		elif self.type == 4:
			self.value = state_literal()
			
		self.value.randomize()


	def generate_code(self):
		return self.value.generate_code()
