from switch_label import switch_label
from randomizer import randomizer
from common import common


class switch_casse(object):
	type = 'switch_casse'
	switch_label = None
	block_statement = None

	# switchCase
	# : switchLabel ':' blockStatement
	# | switchLabel ':'
	# ;

	def __init__(self, switch_label=None, block_statement=None):
		self.switch_label = switch_label
		self.block_statement = block_statement

	def randomize(self):
		self.switch_label = switch_label()
		self.switch_label.randomize()
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.block_statement = None
		elif rnd == 1:
			from block_statement import block_statement
			self.block_statement = block_statement()
			self.block_statement.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		code += self.switch_label.generate_code() + ':'
		if self.block_statement is not None:
			code += self.block_statement.generate_code()
		return code
