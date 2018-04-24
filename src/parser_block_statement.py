from opt_annotations import opt_annotations
from parser_statements import parser_statements

class parser_block_statement(object):
	type = 'parser_block_statement'
	opt_annotations = None
	parser_statements = None

	# parserBlockStatement
	# : optAnnotations '{' parserStatements '}'
	# ;

	def __init__(self, opt_annotations=None, parser_statements=None):
		self.opt_annotations = opt_annotations
		self.parser_statements = parser_statements

	def randomize(self):
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.parser_statements = parser_statements()
		self.parser_statements.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' { ' + self.parser_statements.generate_code() + ' } '
