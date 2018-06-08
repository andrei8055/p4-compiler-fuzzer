from common import common


class bool(object):
	name = 'bool'

	def get_name(self):
		return self.name

	def get_ref_type(self):
		return "bool"

	def generate_code(self):
		common.usedCodeGenerator(self)
		return 'bool'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code_ref(self):
		return 'bool'