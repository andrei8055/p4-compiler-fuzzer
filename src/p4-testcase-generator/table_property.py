from key_element_list import key_element_list
from action_list import action_list
from entries_list import entries_list
from opt_annotations import opt_annotations
from initializer import initializer
from randomizer import randomizer
from common import common


class table_property(object):
	type = 'table_property'
	opt_annotations = None
	value = None
	const_initializer = False

	# tableProperty
	# : KEY '=' '{' keyElementList '}'
	# | ACTIONS '=' '{' actionList '}'
	# | CONST ENTRIES '=' '{' entriesList '}' / * immutable entries * /
	# | optAnnotations CONST IDENTIFIER'='initializer';'
	# | optAnnotations IDENTIFIER'=' initializer';'
	# ;

	def __init__(self, opt_annotations=None, value=None, const_initializer=False):
		self.opt_annotations = opt_annotations
		self.value = value
		self.const_initializer = const_initializer

	def randomize(self):
		rnd = randomizer.randint(0, 4)
		if rnd == 0:
			self.value = key_element_list()
		elif rnd == 1:
			self.value = action_list()
		elif rnd == 2:
			self.value = entries_list()
		elif rnd == 3:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.const_initializer = True
			self.value = initializer()
		elif rnd == 4:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.value = initializer()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		if type(self.value).__name__ == 'key_element_list':
			code += 'key = { ' + self.value.generate_code() + '} '
		elif type(self.value).__name__ == 'action_list':
			code += 'actions = { ' + self.value.generate_code() + '} '
		elif type(self.value).__name__ == 'entries_list':
			code += 'const entries = { ' + self.value.generate_code() + '} '
		elif type(self.value).__name__ == 'initializer':
			code += self.opt_annotations.generate_code() + ' '
			if self.const_initializer:
				code += 'const '
			code += 'identifier = { ' + self.value.generate_code() + '} '
		else:
			code += 'ERROR in table_property - unknown type'
		return code
