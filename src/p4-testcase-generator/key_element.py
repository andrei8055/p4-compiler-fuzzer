from expression import expression
from name import name
from opt_annotations import opt_annotations
from common import common


class key_element(object):
	type = 'table_key'
	expression = None
	name = None
	opt_annotations = None

	# keyElement
	# : expression ':' name optAnnotations';'
	# ;

	def __init__(self, expression=None, name=None, opt_annotations=None):
		self.expression = expression
		self.name = name
		self.opt_annotations = opt_annotations

	def get_name(self):
		return self.name

	def get_expression(self):
		return self.expression

	def get_type(self):
		return self.type

	def randomize(self):
		common.usedRandomize()
		self.expression = expression()
		self.expression.randomize()
		self.name = name()
		self.name.randomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.expression.generate_code() + ':' + self.name.generate_code() + ' ' + self.opt_annotations.generate_code()
