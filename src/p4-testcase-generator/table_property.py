from key_element_list import key_element_list
from action_list import action_list
from entries_list import entries_list
from opt_annotations import opt_annotations
from initializer import initializer
from randomizer import randomizer
from common import common


class table_property(object):
	type = None
	types = ["key", "actions", "entries", "constIdentifier", "identifier"]
	probabilities = [50, 50, 0, 0, 0]
	opt_annotations = None
	value = None
	const_initializer = False

	force_type = None

	# tableProperty
	# : KEY '=' '{' keyElementList '}'
	# | ACTIONS '=' '{' actionList '}'
	# | CONST ENTRIES '=' '{' entriesList '}' / * immutable entries * /
	# | optAnnotations CONST IDENTIFIER'='initializer';'
	# | optAnnotations IDENTIFIER'=' initializer';'
	# ;

	def __init__(self, opt_annotations=None, value=None, const_initializer=False, force_type=None):
		self.opt_annotations = opt_annotations
		self.value = value
		self.const_initializer = const_initializer
		self.force_type = force_type

	def randomize(self):
		tries = 0
		while True:
			self.type = randomizer.getRandom(self.probabilities)
			if tries > 100:
				self.force_type = 1
			if self.force_type is not None:
				self.type = self.force_type
				if self.type == 0:
					tries += 1
					self.value = key_element_list()
					self.value.randomize()
				elif self.type == 1:
					self.value = action_list()
					self.value.randomize()
				elif self.type == 2:
					self.value = entries_list()
					self.value.randomize()
				elif self.type == 3:
					self.opt_annotations = opt_annotations()
					self.opt_annotations.randomize()
					self.const_initializer = True
					self.value = initializer()
					self.value.randomize()
				elif self.type == 4:
					self.opt_annotations = opt_annotations()
					self.opt_annotations.randomize()
					self.value = initializer()
					self.value.randomize()
				if not self.filter():
					break

	def filter(self):
		if self.type == 0:
			if len(self.value.element_list) == 0:
				return True
		return False

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		if self.type == 0:
			code += 'key = { ' + self.value.generate_code() + '} '
		elif self.type == 1:
			code += 'actions = { ' + self.value.generate_code() + '} '
		elif self.type == 2:
			code += 'const entries = { ' + self.value.generate_code() + '} '
		elif self.type == 3 or self.type == 4:
			code += self.opt_annotations.generate_code() + ' '
			if self.const_initializer:
				code += 'const '
			code += 'identifier = { ' + self.value.generate_code() + '} '
		else:
			code += 'ERROR in table_property - unknown type'
		return code
