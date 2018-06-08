from common import common


class exit_statement(object):
	type = 'exit_statement'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		common.usedCodeGenerator(self)
		return 'exit;'
