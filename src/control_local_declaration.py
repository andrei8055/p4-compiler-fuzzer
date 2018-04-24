import random
from constant_declaration import constant_declaration
from action_declaration import action_declaration
from table_declaration import table_declaration
from instantiation import instantiation
from variable_declaration import variable_declaration


class control_local_declaration(object):
	type = 'control_local_declaration'
	value = None

	# controlLocalDeclaration
	# : constantDeclaration
	# | actionDeclaration
	# | tableDeclaration
	# | instantiation
	# | variableDeclaration
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = random.randint(0, 4)
		if rnd == 0:
			self.value = constant_declaration()
		elif rnd == 1:
			self.value = action_declaration()
		elif rnd == 2:
			self.value = table_declaration()
		elif rnd == 3:
			self.value = instantiation()
		elif rnd == 4:
			self.value = variable_declaration()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
