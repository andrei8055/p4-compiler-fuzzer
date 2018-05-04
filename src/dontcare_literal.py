from common import common


class dontcare_literal(object):
	type = 'dontcare_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "_"
