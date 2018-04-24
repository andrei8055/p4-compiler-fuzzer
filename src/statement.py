from empty_statement import empty_statement
from conditional_statement import conditional_statement
from direct_application import direct_application
from assignment_or_method_call_statement import assignment_or_method_call_statement
from block_statement import block_statement
from exit_statement import exit_statement
from return_statement import return_statement
from switch_statement import switch_statement
import random

class statement(object):
	type = 'statement'
	value = None

	# statement
	# : assignmentOrMethodCallStatement
	# | directApplication
	# | conditionalStatement
	# | emptyStatement
	# | blockStatement
	# | exitStatement
	# | returnStatement
	# | switchStatement
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = random.randint(0, 7)
		if rnd == 0:
			self.value = assignment_or_method_call_statement()
		elif rnd == 1:
			self.value = direct_application()
		elif rnd == 2:
			self.value = conditional_statement()
		elif rnd == 3:
			self.value = empty_statement()
		elif rnd == 4:
			self.value = block_statement()
		elif rnd == 5:
			self.value = exit_statement()
		elif rnd == 6:
			self.value = return_statement()
		elif rnd == 7:
			self.value = switch_statement()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()

