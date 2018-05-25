from common import common


class empty_literal(object):
	type = 'empty_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return ""
