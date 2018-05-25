from common import common


class type_literal(object):
	type = 'type_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "type"
