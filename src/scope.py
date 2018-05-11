class scope(object):

	scope_stack = []

	@staticmethod
	def create_new_scope():
		new_scope = {
			"types": [],
			"variables": []
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
	def insert_type(name,type):
		local_scope = scope.get_local()
		local_scope["types"].append({name: { "type": type }})

	@staticmethod
	def get_available_types():
		available_types = []
		for local_scope in scope.scope_stack:
			available_types.extend(local_scope["types"])
		return available_types
