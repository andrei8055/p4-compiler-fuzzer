from randomizer import randomizer
from constant_declaration import constant_declaration
from variable_declaration import variable_declaration
from assignment_or_method_call_statement import assignment_or_method_call_statement
from direct_application import direct_application
from parser_block_statement import parser_block_statement
from common import common


class parser_statement(object):
	type = None
	types = ["assignmentOrMethodCallStatement", "directApplication", "parserBlockStatement", "constantDeclaration", "variableDeclaration"]
	probabilities = [0, 0, 30, 35, 35]

	value = None

	# parserStatement
	# : assignmentOrMethodCallStatement
	# | directApplication
	# | parserBlockStatement
	# | constantDeclaration
	# | variableDeclaration
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = assignment_or_method_call_statement()
		elif self.type == 1:
			self.value = direct_application()
		elif self.type == 2:
			self.value = parser_block_statement()
		elif self.type == 3:
			self.value = constant_declaration()
		elif self.type == 4:
			self.value = variable_declaration()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
