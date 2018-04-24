from opt_annotations import opt_annotations
from function_prototype import function_prototype


class extern_declaration_function(object):
	type = 'extern_declaration_function'

	opt_annotations = None
	function_prototype = None

	# | optAnnotations EXTERN functionPrototype ';'

	def __init__(self, opt_annotations=None, function_prototype=None):
		self.opt_annotations = opt_annotations
		self.function_prototype = function_prototype

	def randomize(self):
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.function_prototype = function_prototype()
		self.function_prototype.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' extern ' + self.function_prototype.generate_code()
