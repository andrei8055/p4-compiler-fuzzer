from common import common


class table_const_entries(object):
	type = 'table_key'

	def __init__(self):
		pass

	def get_type(self):
		pass

	def randomize(self):
		common.usedRandomize()
		pass

	#  CONST ENTRIES '=' '{' entriesList '}' /* immutable entries */
	def generate_code(self):
		common.usedCodeGenerator(self)
		pass