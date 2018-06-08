from type_argument_list import type_argument_list
from common import common


class tuple_type(object):
	type = 'tuple_type'
	type_argument_list = None

	# tupleType
	# : TUPLE '<' typeArgumentList '>' ;

	def __init__(self, type_argument_list=None):
		self.type_argument_list = type_argument_list

	def randomize(self):
		common.usedRandomize()
		self.type_argument_list = type_argument_list()
		self.type_argument_list.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return 'tuple <' + self.type_argument_list.generate_code() + '>'
