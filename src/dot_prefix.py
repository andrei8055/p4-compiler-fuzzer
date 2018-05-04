from common import common


class dot_prefix(object):
	type = 'dot_prefix'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "."
