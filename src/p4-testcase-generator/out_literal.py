from common import common


class out_literal(object):
	type = 'out_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "out"
