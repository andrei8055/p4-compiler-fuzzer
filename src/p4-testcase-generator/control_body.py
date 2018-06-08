from block_statement import block_statement
from common import common


class control_body(object):
	type = 'control_body'
	block_statement = None

	# controlBody
	# : blockStatement
	# ;

	def __init__(self, block_statement=None):
		self.block_statement = block_statement

	def randomize(self):
		common.usedRandomize()
		self.block_statement = block_statement()
		self.block_statement.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.block_statement.generate_code()
