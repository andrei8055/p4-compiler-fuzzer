from randomizer import randomizer
from constant_declaration import constant_declaration
from variable_declaration import variable_declaration
from instantiation import instantiation
from common import common


class parser_local_element(object):
	type = 'parser_local_element'
	value = None

	# parserLocalElement
	# : constantDeclaration
	# | variableDeclaration
	# | instantiation
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = randomizer.randint(0, 2)
		if rnd == 0:
			self.value = constant_declaration()
		elif rnd == 1:
			self.value = variable_declaration()
		elif rnd == 2:
			self.value = instantiation()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
