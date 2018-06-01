from randomizer import randomizer
from scope import scope
from type_ref import type_ref
from non_type_name import non_type_name


class extern_variable_creation(object):
	def __init__(self):
		self.specializations_refs = []
		pass

	non_type_name = None
	extern_name = None
	specializations_refs = None

	def randomize(self):
		available_externs = scope.get_available_types(only_type="extern")
		while True:
			self.extern_name = available_externs.keys()[randomizer.randint(0, len(available_externs)-1)]
			self.non_type_name = non_type_name()
			self.non_type_name.randomize()
			specializations = available_externs[self.extern_name]["specializations"]
			for x in range(0, specializations):
				while True:
					_type_ref = type_ref()
					_type_ref.randomize()
					if not self.specialization_filter(_type_ref):
						break
				self.specializations_refs.append(_type_ref)
			if not self.filter():
				break
		scope.insert_variable(self.non_type_name.generate_code(), "extern_variable")

	def generate_code(self):
		code = ""
		code += self.extern_name
		if len(self.specializations_refs) > 0:
			code += "<"
			for i, specialization_ref in enumerate(self.specializations_refs):
				code += specialization_ref.generate_code()
				if i < len(self.specializations_refs) - 1:
					code += ", "
			code += ">() "
			code += self.non_type_name.generate_code() + ";\n\n"
		return code

	def filter(self):
		if self.non_type_name.generate_code() in scope.get_available_types() or self.non_type_name.generate_code() in scope.get_available_variables():
			return True
		return False

	def specialization_filter(self, specialization_ref):
		if specialization_ref.get_type() == 'specializedType':
			return True
		if specialization_ref.get_type() == 'headerStackType':
			return True
		return False

