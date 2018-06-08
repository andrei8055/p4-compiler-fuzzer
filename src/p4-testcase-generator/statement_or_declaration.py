from variable_declaration import variable_declaration
from constant_declaration import constant_declaration
from statement import statement
from instantiation import instantiation
from randomizer import randomizer
from common import common


class statement_or_declaration(object):
	type = 'statement_or_declaration'
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
		rnd = randomizer.randint(0, 3)
		if rnd == 0:
			self.value = variable_declaration()
		elif rnd == 1:
			self.value = constant_declaration()
		elif rnd == 2:
			self.value = statement()
		elif rnd == 3:
			self.value = instantiation()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
