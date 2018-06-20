from randomizer import randomizer
from scope import scope
from action_declaration import action_declaration
from table_declaration import table_declaration
from common import common


class control_declaration_creation(object):

	min_random_actions = 1
	max_random_actions = 25

	min_random_tables = 1
	max_random_tables = 25

	action_declarations = None
	table_declarations = None

	def __init__(self):
		self.action_declarations = []
		self.table_declarations = []

	def randomize(self):
		rnd = randomizer.randint(self.min_random_actions, self.max_random_actions)
		for x in range(0, rnd):
			_action_declaration = action_declaration()
			_action_declaration.randomize()
			self.action_declarations.append(_action_declaration)
			scope.insert_action(_action_declaration.name.generate_code(), _action_declaration)
		rnd = randomizer.randint(self.min_random_tables, self.max_random_tables)
		for x in range(0, rnd):
			_table_declaration = table_declaration()
			_table_declaration.randomize()
			self.table_declarations.append(_table_declaration)
			scope.insert_table(_table_declaration.name.generate_code(), _table_declaration)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ""
		for _action_declaration in self.action_declarations:
			code += _action_declaration.generate_code()
		for _table_declaration in self.table_declarations:
			code += _table_declaration.generate_code()
		return code

