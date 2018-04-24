from annotations import annotations
from name import name
from type_ref import type_ref
from opt_initializer import opt_initializer


class variable_declaration(object):
	type = 'variable_declaration'

	annotations = None
	type_ref = None
	name = None
	opt_initializer = None

	# variableDeclaration
	# : annotations typeRef name optInitializer';'
	# | typeRef name optInitializer';'
	# ;

	def __init__(self, annotations=None, type_ref=None, name=None, opt_initializer=None):
		self.annotations = annotations
		self.type_ref = type_ref
		self.name = name
		self.opt_initializer = opt_initializer

	def randomize(self):
		self.annotations = annotations()
		self.annotations.randomize()
		self.type_ref = type_ref()
		self.type_ref.randomize()
		self.name = name()
		self.name.randomize()
		self.opt_initializer = opt_initializer()
		self.opt_initializer.randomize()

	def generate_code(self):
		code = ''
		if self.annotations is not None:
			code += self.annotations.generate_code() + ' '
		code += self.type_ref.generate_code() + ' ' + self.name.generate_code() + ' ' + self.opt_initializer.generate_code() + ';'
		return code