from common import common


class error_literal(object):
	type = 'error_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		common.usedCodeGenerator(self)
		return "error"
