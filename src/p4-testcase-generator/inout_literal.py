from common import common


class inout_literal(object):
	type = 'inout_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "inout"
