from opt_annotations import opt_annotations
from name import name
from type_ref import type_ref
from initializer import initializer
from common import common


class constant_declaration(object):
	type = 'constant_declaration'

	opt_annotations = None
	type_ref = None
	name = None
	initializer = None

	# constantDeclaration
	# : optAnnotations CONST typeRef name'='initializer';'
	# ;

	def __init__(self, opt_annotations=None, type_ref=None, name=None, initializer=None):
		self.opt_annotations = opt_annotations
		self.type_ref = type_ref
		self.name = name
		self.initializer = initializer

	def randomize(self):
		common.usedRandomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.type_ref = type_ref()
		self.type_ref.randomize()
		self.name = name()
		self.name.randomize()
		self.initializer = initializer()
		self.initializer.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' const ' + self.type_ref.generate_code() + ' ' + self.name.generate_code() + ' = ' + self.initializer.generate_code()
