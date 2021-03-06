from opt_annotations import opt_annotations
from name import name
from parameter_list import parameter_list
from block_statement import block_statement
from common import common
from scope import scope


class action_declaration(object):
	type = 'action_declaration'

	opt_annotations = None
	name = None
	parameter_list = None
	block_statement = None

	# actionDeclaration
	# : optAnnotations ACTION name '(' parameterList ')' blockStatement
	# ;

	def __init__(self, opt_annotations=None, name=None, parameter_list=None, block_statement=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.parameter_list = parameter_list
		self.block_statement = block_statement

	def randomize(self):
		common.usedRandomize()
		while True:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.name = name()
			self.name.randomize()
			self.parameter_list = parameter_list()
			#self.parameter_list.randomize()
			self.block_statement = block_statement()
			self.block_statement.randomize()
			if not self.filter():
				break

	def filter(self):
		if self.name.generate_code() in scope.get_available_types():
			return True
		if self.name.generate_code() in scope.get_available_variables():
			return True
		if self.name.generate_code() in scope.get_available_states():
			return True
		if self.name.generate_code() in scope.get_available_actions():
			return True
		return False

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.opt_annotations.generate_code() + '\naction ' + self.name.generate_code() + '(' + self.parameter_list.generate_code() + ')' + '\n' + self.block_statement.generate_code() + '\n\n'
