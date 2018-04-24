from type_ref import type_ref
from derived_type_declaration import derived_type_declaration
from name import name
from annotations import annotations
import random

class typedef_declaration(object):
	type = 'typedef_declaration'
	annotation = None
	value = None
	name = None

	# typedefDeclaration
	# : annotations TYPEDEF typeRef name';'
	# | TYPEDEF typeRef name ';'
	# | annotations TYPEDEF derivedTypeDeclaration name';'
	# | TYPEDEF derivedTypeDeclarationame';'
	# ;

	def __init__(self, annotation=None, value=None, name=None):
		self.annotation = annotation
		self.value = value
		self.name = name

	def randomize(self):
		rnd = random.randint(0, 3)
		if rnd == 0:
			self.annotation = annotations()
			self.annotation.randomize()
			self.value = type_ref()
			self.value.randomize()
			self.name = name()
			self.name.randomize()
		elif rnd == 1:
			self.annotation = None
			self.value = type_ref()
			self.value.randomize()
			self.name = name()
			self.name.randomize()
		elif rnd == 2:
			self.annotation = annotations()
			self.annotation.randomize()
			self.value = derived_type_declaration()
			self.value.randomize()
			self.name = name()
			self.name.randomize()
		elif rnd == 3:
			self.annotation = None
			self.value = derived_type_declaration()
			self.value.randomize()
			self.name = None
		self.value.randomize()

	def generate_code(self):
		code = ''
		if self.annotation is not None:
			code += self.annotation.generate_code() + ' '
		code += self.value.generate_code() + ' '
		if self.name is not None:
			code += self.name.generate_code()
		code += ';'
		return code

