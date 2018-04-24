from opt_annotations import opt_annotations
from direction import direction
from type_ref import type_ref
from name import name


class parameter(object):
	opt_annotations = None
	direction = None
	type = 'parameter'
	type_ref = None
	name = None

	# parameter
	# : optAnnotations direction typeRef name
	# ;

	def __init__(self, opt_annotations=None, direction=None, type_ref=None, name=None):
		self.opt_annotations = opt_annotations
		self.direction = direction
		self.type_ref = type_ref
		self.name = name

	def get_name(self):
		return self.name

	def get_direction(self):
		return self.direction

	def get_type_ref(self):
		return self.type_ref

	def randomize(self):
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.direction = direction()
		self.direction.randomize()
		self.type_ref = type_ref()
		self.type_ref.randomize()
		self.name = name()
		self.name.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' ' + self.direction.generate_code() + ' ' + self.type_ref.generate_code() + ' ' + self.name.generate_code()
