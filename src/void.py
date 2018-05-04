from common import common


class void(object):
	name = 'void'

	def get_name(self):
		return self.name

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return 'void'

	def generate_code_ref(self):
		return 'void'