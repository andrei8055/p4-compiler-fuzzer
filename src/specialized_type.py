from type_argument_list import type_argument_list
from prefixed_type import prefixed_type
from common import common


class specialized_type(object):
	prefixed_type = None
	type_argument_list = None

	# specializedType
	# : prefixedTYpe '<' typeArgumentList '>'
	# ;

	def __init__(self, prefixed_type=None, type_argument_list=None):
		self.prefixed_type = prefixed_type
		self.type_argument_list = type_argument_list

	def randomize(self):
		self.prefixed_type = prefixed_type()
		self.prefixed_type.randomize()
		if self.prefixed_type.value is not None:
			self.type_argument_list = type_argument_list()
			self.type_argument_list.randomize()
		else:
			self.prefixed_type  = None

	def generate_code(self):
		return self.prefixed_type.generate_code() + '<' + self.type_argument_list.generate_code() + '>'
