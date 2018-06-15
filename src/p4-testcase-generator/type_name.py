from prefixed_type import prefixed_type
from common import common


class type_name(object):
	type = 'type_name'
	prefixed_type = None

	# typeName
	# : prefixedType
	# ;

	def __init__(self, prefixed_type=None):
		self.prefixed_type = prefixed_type

	def get_ref_type(self):
		return self.prefixed_type.get_ref_type()

	def get_type_decl(self):
		return self.prefixed_type.get_type_decl()

	def randomize(self):
		self.prefixed_type = prefixed_type()
		self.prefixed_type.randomize()
		if self.prefixed_type.value is None:
			self.prefixed_type = None

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.prefixed_type.generate_code()
