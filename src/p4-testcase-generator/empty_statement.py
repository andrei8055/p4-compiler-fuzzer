from common import common


class empty_statement(object):
	type = 'empty_statement'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return ';'
