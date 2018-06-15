from randomizer import randomizer
from name import name
from select_expression import select_expression
from common import common
from scope import scope


class state_expression(object):
	type = None
	types = ["name", "selectExpression"]
	probabilities = [50, 50]
	value = None

	# stateExpression
	# : name ';'
	# | selectExpression
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		while True:
			self.type = randomizer.getRandom(self.probabilities)
			if self.type == 0:
				available_states = scope.get_available_states()
				self.value = available_states.keys()[randomizer.randint(0, len(available_states) - 1)]
			elif self.type == 1:
				self.value = select_expression()
				self.value.randomize()
			if not self.filter():
				break

	def filter(self):
		if self.type == 1 and self.value.member is None:
			return True
		return False

	def generate_code(self):
		common.usedCodeGenerator(self)
		if self.type == 0:
			return self.value + ';'
		elif self.type == 1:
			return self.value.generate_code()
		else:
			return 'ERROR - invalid value type'
