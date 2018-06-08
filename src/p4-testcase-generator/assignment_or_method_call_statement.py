from assignment_statement import assignment_statement
from method_call_statement import method_call_statement
from randomizer import randomizer
from common import common


class assignment_or_method_call_statement(object):
	type = 'assignment_or_method_call_statement'
	value = None

	# assignmentOrMethodCallStatement
	# : lvalue '(' argumentList ')' ';'
	# | lvalue '<'typeArgumentList'>' '('argumentList ')' ';'
	# | lvalue '=' expression ';'
	# ;
	#
	# *split into
	# assignmentStatement
	# methodCallStatement

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.value = assignment_statement()
		elif rnd == 1:
			self.value = method_call_statement()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
