from header_type_declaration import header_type_declaration
from header_union_declaration import header_union_declaration
from struct_type_declaration import struct_type_declaration
from enum_declaration import enum_declaration
import random

class derived_type_declaration(object):
	type = 'derived_type_declaration'
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
		rnd = random.randint(0, 3)
		if rnd == 0:
			self.value = header_type_declaration()
		elif rnd == 1:
			self.value = header_union_declaration()
		elif rnd == 2:
			self.value = struct_type_declaration(None)
		elif rnd == 3:
			self.value = enum_declaration(None)
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
