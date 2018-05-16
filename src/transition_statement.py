from randomizer import randomizer
from state_expression import state_expression


class transition_statement(object):
	type = 'transition_statement'
	state_expression = None

	# transitionStatement
	# : / *empty * /
	# | TRANSITION stateExpression
	# ;

	def __init__(self, state_expression=None):
		self.state_expression = state_expression

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.state_expression = None
		else:
			self.state_expression = state_expression()
			self.state_expression.randomize()

	def generate_code(self):
		if self.state_expression is not None:
			return 'transition' + ' ' + self.state_expression.generate_code()
		else:
			return ''
