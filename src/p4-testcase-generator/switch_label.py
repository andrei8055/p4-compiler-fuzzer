from default_literal import default_literal
from name import name
from randomizer import randomizer
from common import common


class switch_label(object):
	type = 'switch_label'
	value = None

	# switchLabel
	# : name
	# | DEFAULT
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.value = name()
		elif rnd == 1:
			self.value = default_literal()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
