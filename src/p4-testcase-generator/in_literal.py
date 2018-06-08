from common import common


class in_literal(object):
	type = 'in_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		common.usedCodeGenerator(self)
		return "in"
