from common import common


class key_literal(object):
	type = 'key_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		common.usedCodeGenerator(self)
		return "key"
