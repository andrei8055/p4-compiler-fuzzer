from variable_declaration import variable_declaration
from constant_declaration import constant_declaration
from statement import statement
from instantiation import instantiation
from randomizer import randomizer
from common import common


class statement_or_declaration(object):
	type = None
	types = ["variableDeclaration", "constantDeclaration", "statement", "instantiation"]
	probabilities = [50, 50, 0, 0]
	value = None

	# statementOrDeclaration
	# : variableDeclaration
	# | constantDeclaration
	# | statement
	# | instantiation
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = variable_declaration()
		elif self.type == 1:
			self.value = constant_declaration()
		elif self.type == 2:
			self.value = statement()
		elif self.type == 3:
			self.value = instantiation()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
