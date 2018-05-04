from common import common


class return_statement(object):
	type = 'return_statement'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return 'return;'
