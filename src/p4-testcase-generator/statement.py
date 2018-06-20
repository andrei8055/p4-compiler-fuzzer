from empty_statement import empty_statement
from conditional_statement import conditional_statement
from direct_application import direct_application
from assignment_or_method_call_statement import assignment_or_method_call_statement
from exit_statement import exit_statement
from return_statement import return_statement
from switch_statement import switch_statement
from randomizer import randomizer
from common import common


class statement(object):
	type = None
	types = ["assignmentOrMethodCallStatement", "directApplication", "conditionalStatement", "emptyStatement", "blockStatement", "exitStatement", "returnStatement", "switchStatement"]
	probabilities = [100, 0, 0, 0, 0, 0, 0, 0]
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
		from block_statement import block_statement
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = assignment_or_method_call_statement()
		elif self.type == 1:
			self.value = direct_application()
		elif self.type == 2:
			self.value = conditional_statement()
		elif self.type == 3:
			self.value = empty_statement()
		elif self.type == 4:
			self.value = block_statement()
		elif self.type == 5:
			self.value = exit_statement()
		elif self.type == 6:
			self.value = return_statement()
		elif self.type == 7:
			self.value = switch_statement()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()

