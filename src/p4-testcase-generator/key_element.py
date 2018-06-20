from opt_annotations import opt_annotations
from common import common
from scope import scope
from randomizer import randomizer


class key_element(object):
	type = 'table_key'
	parameter = None
	member = None
	name = None
	opt_annotations = None

	algorithms = ["exact", "ternary"]

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
		available_parameters = scope.get_available_parameters(["struct", "header"])
		if len(available_parameters):
			self.parameter = available_parameters.keys()[randomizer.randint(0, len(available_parameters) - 1)]
			_parameter = available_parameters[self.parameter]["object"].type_ref.get_type_decl()
			if len(_parameter.struct_field_list.field_list):
				_field_list = []
				for _field in _parameter.struct_field_list.field_list:
					if _field.type_ref.type == 0 and _field.type_ref.get_ref_type() != "varbit":
						_field_list.append(_field)
				if len(_field_list):
					self.member = _field_list[randomizer.randint(0, len(_field_list) - 1)]
		self.name = self.algorithms[randomizer.randint(0, len(self.algorithms) - 1)]
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ""
		if self.member is not None:
			code += self.parameter
			code += '.' + self.member.name.generate_code()
			code += ' : ' + self.name + ' ' + self.opt_annotations.generate_code() + ';\n'
		return code
