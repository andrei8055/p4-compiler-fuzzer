from common import common



class state_literal(object):
	type = 'state_literal'

	def randomize(self):
		common.usedRandomize()
		pass

	def generate_code(self):
		return "state"
