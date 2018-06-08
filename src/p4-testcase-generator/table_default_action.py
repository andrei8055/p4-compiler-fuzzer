from common import common


class table_default_action(object):
	value = 'NoAction()'
	type = 'table_default_action'

	name_min_length = 1
	name_max_length = 50

	def __init__(self, value=''):
		self.value = value

	def get_value(self):
		return self.value

	def get_type(self):
		return self.type

	def randomize(self):
		common.usedRandomize()
		pass

	#  default_action = value ';'
	def generate_code(self):
		common.usedCodeGenerator(self)
		code = 'default_action = ' + self.value + ';'
		return code