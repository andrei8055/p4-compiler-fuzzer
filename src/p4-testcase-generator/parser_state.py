from opt_annotations import opt_annotations
from parser_statements import parser_statements
from transition_statement import transition_statement
from name import name
from common import common
from common import common


class parser_state(object):
	opt_annotations = None
	name = None
	parser_statements = None
	transition_statement = None
	type = 'parser_state'

	# parserState
	# : optAnnotations STATE name '{' parserStatements transitionStatement '}'
	# ;

	def __init__(self, opt_annotations=None, name=None, parser_statements=None, transition_statement=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.parser_statements = parser_statements
		self.transition_statement = transition_statement

	def get_name(self):
		return self.name

	def randomize(self):
		common.usedRandomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.name = name()
		self.name.randomize()
		self.parser_statements = parser_statements()
		self.parser_statements.randomize()
		self.transition_statement = transition_statement()
		self.transition_statement.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.opt_annotations.generate_code() + ' state ' + self.name.generate_code() + ' { ' +self.parser_statements.generate_code() + ' ' + self.transition_statement.generate_code() + '} '
