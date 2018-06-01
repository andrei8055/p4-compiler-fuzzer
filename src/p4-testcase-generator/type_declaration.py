from derived_type_declaration import derived_type_declaration
from typedef_declaration import typedef_declaration
from parser_type_declaration import parser_type_declaration
from control_type_declaration import control_type_declaration
from package_type_declaration import package_type_declaration
from randomizer import randomizer


class type_declaration(object):
	type = None
	types = ["derivedTypeDeclaration", "typedefDeclaration", "parserTypeDeclaration", "controlTypeDeclaration",
			 "packageTypeDeclaration"]
	probabilities = [20, 20, 20, 20, 20]
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
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = derived_type_declaration()
		elif self.type == 1:
			self.value = typedef_declaration()
		elif self.type == 2:
			self.value = parser_type_declaration(None)
		elif self.type == 3:
			self.value = control_type_declaration(None)
		elif self.type == 4:
			self.value = package_type_declaration(None)
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
