from common import common
from randomizer import randomizer


class bool(object):
	name = 'bool'

	def get_name(self):
		return self.name

	def get_ref_type(self):
		return "bool"

	def get_type_decl(self):
		return self

	def generate_code(self):
		common.usedCodeGenerator(self)
		return 'bool'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code_ref(self):
		return 'bool'

	def generate_literal(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			return "false"
		return "true"
