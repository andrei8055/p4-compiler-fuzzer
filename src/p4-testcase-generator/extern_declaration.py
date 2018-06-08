from opt_annotations import opt_annotations
from non_type_name import non_type_name
from opt_type_parameters import opt_type_parameters
from method_prototypes import method_prototypes
from function_prototype import function_prototype
from randomizer import randomizer
from scope import scope
from common import common


class extern_declaration(object):
	type = None
	types = ["externObject", "externFunction"]
	# TODO: allow externFunction as well
	probabilities = [100, 0]
	opt_annotations = None
	non_type_name = None
	opt_type_parameters = None
	method_prototypes = None
	function_prototype = None

	# externDeclaration
	# : optAnnotations EXTERN nonTypeName optTypeParameters '{' methodPrototypes '}'
	# | optAnnotations EXTERN functionPrototype ';'
	# ;

	def __init__(self):
		pass

	def get_type(self):
		return self.types[self.type]

	def randomize(self):
		specializations = 0
		scope.start_local()
		while True:
			self.type = randomizer.getRandom(self.probabilities)
			if self.type == 0:
				self.opt_annotations = opt_annotations()
				self.opt_annotations.randomize()
				self.non_type_name = non_type_name()
				self.non_type_name.randomize()
				self.opt_type_parameters = opt_type_parameters()
				self.opt_type_parameters.randomize()
			elif self.type == 1:
				self.opt_annotations = opt_annotations()
				self.opt_annotations.randomize()
				self.function_prototype = function_prototype()
				self.function_prototype.randomize()
			if not self.filter():
				break
		if self.type == 0:
			if self.opt_type_parameters.type_parameter_list is not None:
				for parameter in self.opt_type_parameters.type_parameter_list.parameter_list:
					scope.insert_type(parameter.generate_code(), "template")
					specializations += 1
			self.method_prototypes = method_prototypes()
			self.method_prototypes.randomize()
		scope.stop_local()
		scope.insert_type(self.non_type_name.generate_code(), "extern", specializations)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ""
		if self.type == 0:
			code += self.opt_annotations.generate_code()
			code += "extern "
			code += self.non_type_name.generate_code() + " "
			code += self.opt_type_parameters.generate_code()
			code += "{\n"
			code += self.non_type_name.generate_code() + "();\n"
			code += self.method_prototypes.generate_code()
			code += "}\n\n"
		elif self.type == 1:
			code += self.opt_annotations.generate_code()
			code += "extern "
			code += self.function_prototype.generate_code()
			code += ";\n\n"
		return code

	def filter(self):
		if self.non_type_name is not None and self.non_type_name.generate_code() in scope.get_available_types() or self.non_type_name.generate_code() in scope.get_available_variables():
			return True
		if self.opt_type_parameters.type_parameter_list is not None:
			for parameter in self.opt_type_parameters.type_parameter_list.parameter_list:
				if parameter.generate_code() in scope.get_available_types() or parameter.generate_code() in scope.get_available_variables():
					return True
		return False
