from derived_type_declaration import derived_type_declaration
from typedef_declaration import typedef_declaration
from parser_type_declaration import parser_type_declaration
from control_type_declaration import control_type_declaration
from package_type_declaration import package_type_declaration
import random

class type_declaration(object):
	type = 'type_declaration'
	value = None

	# typeDeclaration
	# : derivedTypeDeclaration
	# | typedefDeclaration
	# | parserTypeDeclaration';'
	# | controlTypeDeclaration';'
	# | packageTypeDeclaration';'
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = random.randint(0, 4)
		if rnd == 0:
			self.value = derived_type_declaration()
		elif rnd == 1:
			self.value = typedef_declaration()
		elif rnd == 2:
			self.value = parser_type_declaration(None)
		elif rnd == 3:
			self.value = control_type_declaration(None)
		elif rnd == 4:
			self.value = package_type_declaration(None)
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
