from randomizer import randomizer
from non_type_name import non_type_name
from common import common


class prefixed_non_type_name(object):
	type = 'prefixed_non_type_name'
	prefix = False
	non_type_name = None

	def __init__(self, prefix=False, non_type_name=None):
		self.prefix = prefix
		self.non_type_name = non_type_name

	def randomize(self):
		self.prefix = randomizer.choice([True, False])
		self.non_type_name = non_type_name()
		self.non_type_name.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		if self.prefix:
			code += '.'
		code += self.non_type_name.generate_code()
		return code
