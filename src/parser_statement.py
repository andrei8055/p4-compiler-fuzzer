import random
from constant_declaration import constant_declaration
from variable_declaration import variable_declaration
from assignment_or_method_call_statement import assignment_or_method_call_statement
from direct_application import direct_application
from parser_block_statement import parser_block_statement


class parser_statement(object):
	type = 'parser_statement'
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
		rnd = random.randint(0, 4)
		if rnd == 0:
			self.value = assignment_or_method_call_statement()
		elif rnd == 1:
			self.value = direct_application()
		elif rnd == 2:
			self.value = parser_block_statement()
		elif rnd == 3:
			self.value = constant_declaration()
		elif rnd == 4:
			self.value = variable_declaration()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
