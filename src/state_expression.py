from randomizer import randomizer
from name import name
from select_expression import select_expression


class state_expression(object):
	type = 'state_expression'
	value = None

	# stateExpression
	# : name ';'
	# | selectExpression
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.value = name()
		elif rnd == 1:
			self.value = select_expression()
		self.value.randomize()

	def generate_code(self):
		if type(self.value).__name__ == 'name':
			return self.value.generate_code() + ';'
		elif type(self.value).__name__ == 'select_expression':
			return self.value.generate_code()
		else:
			return 'ERROR - invalid value type'
