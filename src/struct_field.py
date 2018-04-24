from opt_annotations import opt_annotations
from type_ref import type_ref
from name import name


class header_type_declaration(object):
	type = 'header_type_declaration'

	opt_annotations = None
	type_ref = None
	name = None

	# structField
	# : optAnnotations typeRef name';'
	# ;

	def __init__(self, opt_annotations=None, type_ref=None, name=None):
		self.opt_annotations = opt_annotations
		self.type_ref = type_ref
		self.name = name

	def randomize(self):
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.type_ref = type_ref()
		self.type_ref.randomize()
		self.name = name()
		self.name.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' ' + self.type_ref.generate_code() + ' ' + self.name.generate_code() + ';'

