from common import common

class actions_literal(object):
	type = 'actions_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		common.usedCodeGenerator(self)
		return "actions"
