from control_local_declaration import control_local_declaration
from randomizer import randomizer
from common import common


class control_local_declarations(object):
	type = 'control_local_declarations'
	local_declarations_list = []
	min_list_size = 1
	max_list_size = 5

	# controlLocalDeclarations
	# : / *empty * /
	# | controlLocalDeclarations controlLocalDeclaration
	# ;

	def __init__(self, local_declarations_list=None):
		self.local_declarations_list = local_declarations_list if local_declarations_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.local_declarations_list = []
		else:
			rndl = randomizer.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_control_local_declaration = control_local_declaration()
				_control_local_declaration.randomize()
				self.local_declarations_list.append(_control_local_declaration)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for local_declaration in self.local_declarations_list:
			code += local_declaration.generate_code() + ' '
		return code

