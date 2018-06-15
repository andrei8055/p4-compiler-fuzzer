class scope(object):

	scope_stack = []

	@staticmethod
	def create_new_scope():
		new_scope = {
			"types": {},
			"variables": {},
			"states": {},
			"parameters": {}
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
	def insert_type(name, type, object, specializations=0):
		local_scope = scope.get_local()
		local_scope["types"].update({name: {"type": type, "object": object, "specializations": specializations}})

	@staticmethod
	def insert_variable(name, type, object):
		local_scope = scope.get_local()
		local_scope["variables"].update({name: {"type": type, "object": object}})

	@staticmethod
	def insert_state(name, object):
		local_scope = scope.get_local()
		local_scope["states"].update({name: {"object": object}})

	@staticmethod
	def insert_parameter(name, type, object):
		local_scope = scope.get_local()
		local_scope["parameters"].update({name: {"type": type, "object": object}})

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

	@staticmethod
	def get_available_states():
		available_states = {}
		for local_scope in scope.scope_stack:
			available_states.update(local_scope["states"])
		return available_states

	@staticmethod
	def get_available_parameters(only_types=None):
		available_parameters = {}
		for local_scope in scope.scope_stack:
			for local_type in local_scope["parameters"].items():
				if (only_types is not None and local_type[1]["type"] in only_types) or only_types is None:
					available_parameters.update({local_type[0]: local_type[1]})
		return available_parameters
