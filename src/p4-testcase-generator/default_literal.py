from common import common


class default_literal(object):
	type = 'default_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "default"
