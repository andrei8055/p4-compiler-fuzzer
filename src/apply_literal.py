from common import common


class apply_literal(object):
	type = 'apply_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "apply"
