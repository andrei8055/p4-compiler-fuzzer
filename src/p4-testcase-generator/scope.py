class scope(object):

	scope_stack = []

	@staticmethod
	def create_new_scope():
		new_scope = {
			"types": {},
			"variables": {}
		}
		return new_scope

	@staticmethod
	def start_local():
		new_scope = scope.create_new_scope()
		scope.scope_stack.append(new_scope)

	@staticmethod
	def stop_local():
		scope.scope_stack.pop()

	@staticmethod
	def get_local():
		local_scope = scope.scope_stack[-1]
		return local_scope

	@staticmethod
	def insert_type(name, type, specializations=0):
		local_scope = scope.get_local()
		local_scope["types"].update({name: {"type": type, "specializations": specializations}})

	@staticmethod
	def insert_variable(name, type):
		local_scope = scope.get_local()
		local_scope["variables"].update({name: {"type": type}})

	@staticmethod
	def get_available_types(only_type=None):
		available_types = {}
		for local_scope in scope.scope_stack:
			for local_type in local_scope["types"].items():
				if (only_type is not None and local_type[1]["type"] == only_type) or only_type is None:
					available_types.update({local_type[0]: local_type[1]})
		return available_types

	@staticmethod
	def get_available_variables():
		available_variables = {}
		for local_scope in scope.scope_stack:
			available_variables.update(local_scope["variables"])
		return available_variables
