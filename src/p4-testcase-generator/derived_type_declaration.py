from header_type_declaration import header_type_declaration
from header_union_declaration import header_union_declaration
from struct_type_declaration import struct_type_declaration
from enum_declaration import enum_declaration
from randomizer import randomizer


class derived_type_declaration(object):
	type = None
	types = ["headerTypeDeclaration", "headerUnionDeclaration", "structTypeDeclaration", "enumDeclaration"]
	probabilities = [30, 30, 30, 10]
	value = None

	# derivedTypeDeclaration
	# : headerTypeDeclaration
	# | headerUnionDeclaration
	# | structTypeDeclaration
	# | enumDeclaration
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = header_type_declaration()
		elif self.type == 1:
			self.value = header_union_declaration()
		elif self.type == 2:
			self.value = struct_type_declaration()
		elif self.type == 3:
			self.value = enum_declaration()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
