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

	def randomize(self):
		common.usedRandomize()
		self.prefixed_type = prefixed_type()
		self.prefixed_type.randomize()

	def generate_code(self):
		return self.prefixed_type.generate_code()
