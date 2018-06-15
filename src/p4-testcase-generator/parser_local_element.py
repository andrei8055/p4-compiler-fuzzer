from randomizer import randomizer
from constant_declaration import constant_declaration
from variable_declaration import variable_declaration
from instantiation import instantiation
from common import common


class parser_local_element(object):
	type = None
	types = ["constantDeclaration", "variableDeclaration", "instantiation"]
	probabilities = [50, 50, 0]
	value = None

	# parserLocalElement
	# : constantDeclaration
	# | variableDeclaration
	# | instantiation
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = constant_declaration()
		elif self.type == 1:
			self.value = variable_declaration()
		elif self.type == 2:
			self.value = instantiation()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
