from randomizer import randomizer
from constant_declaration import constant_declaration
from extern_declaration import extern_declaration
from action_declaration import action_declaration
from parser_declaration import parser_declaration
from type_declaration import type_declaration
from control_declaration import control_declaration
from instantiation import instantiation
from error_declaration import error_declaration
from match_kind_declaration import match_kind_declaration
from common import common

class declaration(object):
	type = 'declaration'
	value = None

	# declaration
	# : constantDeclaration
	# | externDeclaration
	# | actionDeclaration
	# | parserDeclaration
	# | typeDeclaration
	# | controlDeclaration
	# | instantiation
	# | errorDeclaration
	# | matchKindDeclaration
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = randomizer.randint(0, 8)
		if rnd == 0:
			self.value = constant_declaration()
		elif rnd == 1:
			self.value = extern_declaration()
		elif rnd == 2:
			self.value = action_declaration()
		elif rnd == 3:
			self.value = parser_declaration()
		elif rnd == 4:
			self.value = type_declaration()
		elif rnd == 5:
			self.value = control_declaration()
		elif rnd == 6:
			self.value = instantiation()
		elif rnd == 7:
			self.value = error_declaration()
		elif rnd == 8:
			self.value = match_kind_declaration()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
