from common import common


class bool(object):
	name = 'bool'

	def get_name(self):
		return self.name

	def generate_code(self):
		return 'bool'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code_ref(self):
		return 'bool'