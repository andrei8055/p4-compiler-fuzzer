from struct_type_declaration import struct_type_declaration
from header_type_declaration import header_type_declaration
from extern_declaration import extern_declaration
from extern_variable_creation import extern_variable_creation
from parser_declaration import parser_declaration
from control_declaration import control_declaration
from struct_field_list import struct_field_list
from parser_local_elements import parser_local_elements
from control_declaration_creation import control_declaration_creation
from parser_states import parser_states
from parameter import parameter
from prefixed_type import prefixed_type
from scope import scope
from randomizer import randomizer


class netfpga_random_program_generator(object):

	min_random_structs = 1
	max_random_structs = 25

	min_random_headers = 1
	max_random_headers = 25

	min_random_parsers = 1
	max_random_parsers = 5

	min_random_externs = 1
	max_random_externs = 25

	min_extern_variables = 1
	max_extern_variables = 25

	min_random_controls = 1
	max_random_controls = 5

	struct_name = ""

	def __init__(self):
		pass

	def generate(self):
		scope.start_local()
		code = ""
		code += self.output_seed_comment()
		code += self.generate_netfpga_includes()
		code += self.generate_netfpga_structs()
		code += self.generate_random_structs()
		code += self.generate_random_headers()
		code += self.generate_random_externs()
		code += self.generate_extern_variables()
		code += self.generate_netfpga_parser()
		code += self.generate_random_parsers()
		code += self.generate_netfpga_controls()
		code += self.generate_random_controls()
		code += self.generate_netfpga_init()
		scope.stop_local()
		return code

	def output_seed_comment(self):
		return "//seed: " + str(randomizer.getSeed()) + "\n"

	def generate_netfpga_includes(self):
		return "#include <core.p4>\n#include <sume_switch.p4>\n"


	def generate_netfpga_structs(self):
		parsed_packet = struct_type_declaration(name="Parsed_packet")
		_struct_field_list = struct_field_list(fromObj=parsed_packet)
		_struct_field_list.randomize()
		parsed_packet.struct_field_list = _struct_field_list
		digest_data_t = struct_type_declaration(name="digest_data_t")
		_struct_field_list2 = struct_field_list(fromObj=digest_data_t)
		_struct_field_list2.randomize()
		digest_data_t.struct_field_list = _struct_field_list2
		user_metadata_t = struct_type_declaration(name="user_metadata_t")
		_struct_field_list3 = struct_field_list(fromObj=user_metadata_t)
		scope.start_local()
		_struct_field_list3.randomize()
		scope.stop_local()
		user_metadata_t.struct_field_list = _struct_field_list3
		structs = (parsed_packet, digest_data_t, user_metadata_t)
		code = ""
		for struct in structs:
			code += struct.generate_code()
		return code

	def generate_random_structs(self):
		rnd = randomizer.randint(self.min_random_structs, self.max_random_structs)
		struct_type_declarations = []
		for x in range(0, rnd):
			_struct_type_declaration = struct_type_declaration()
			_struct_type_declaration.randomize()
			struct_type_declarations.append(_struct_type_declaration)
		code = ""
		for _struct_type_declaration in struct_type_declarations:
			code += _struct_type_declaration.generate_code()
		return code

	def generate_random_headers(self):
		rnd = randomizer.randint(self.min_random_headers, self.max_random_headers)
		header_type_declarations = []
		for x in range(0, rnd):
			_header_type_declaration = header_type_declaration()
			_header_type_declaration.randomize()
			header_type_declarations.append(_header_type_declaration)
		code = ""
		for _header_type_declaration in header_type_declarations:
			code += _header_type_declaration.generate_code()
		return code

	def generate_random_externs(self):
		rnd = randomizer.randint(self.min_random_externs, self.max_random_externs)
		extern_declarations = []
		for x in range(0, rnd):
			_extern_declaration = extern_declaration()
			_extern_declaration.randomize()
			extern_declarations.append(_extern_declaration)
		code = ""
		for _extern_declaration in extern_declarations:
			code += _extern_declaration.generate_code()
		return code

	def generate_extern_variables(self):
		rnd = randomizer.randint(self.min_extern_variables, self.max_extern_variables)
		extern_variables = []
		for x in range(0, rnd):
			_extern_variable = extern_variable_creation()
			_extern_variable.randomize()
			extern_variables.append(_extern_variable)
		code = ""
		for _extern_variable in extern_variables:
			code += _extern_variable.generate_code()
		return code

	def generate_netfpga_parser(self):
		available_structs = scope.get_available_types(only_type="struct")
		self.struct_name = available_structs.keys()[randomizer.randint(0, len(available_structs) - 1)]
		scope.start_local()
		_parameter = parameter(type_ref=prefixed_type(value={self.struct_name: available_structs[self.struct_name]}))
		scope.insert_parameter("user_metadata", "struct", _parameter)
		_parser_states = parser_states()
		_parser_states.randomize()
		_parser_local_elements = parser_local_elements()
		_parser_local_elements.randomize()
		code = "parser TopParser(packet_in b,\nout Parsed_packet p,\nout " + self.struct_name + " user_metadata,\nout digest_data_t digest_data,\ninout sume_metadata_t sume_metadata) {\n" + _parser_local_elements.generate_code() + "\n" + _parser_states.generate_code() + "\n}\n\n"
		scope.stop_local()
		return code

	def generate_random_parsers(self):
		rnd = randomizer.randint(self.min_random_parsers, self.max_random_parsers)
		parser_declarations = []
		for x in range(0, rnd):
			_parser_declaration = parser_declaration()
			_parser_declaration.randomize()
			parser_declarations.append(_parser_declaration)
		code = ""
		for _parser_declaration in parser_declarations:
			code += _parser_declaration.generate_code()
		return code

	def generate_netfpga_controls(self):
		available_structs = scope.get_available_types(only_type="struct")
		scope.start_local()
		_parameter = parameter(type_ref=prefixed_type(value={self.struct_name: available_structs[self.struct_name]}))
		scope.insert_parameter("user_metadata", "struct", _parameter)
		scope.start_local()
		_control_local_declarations = control_declaration_creation()
		_control_local_declarations.randomize()
		available_tables = scope.get_available_tables()
		table = available_tables.keys()[randomizer.randint(0, len(available_tables) - 1)]
		scope.stop_local()
		code = "control TopPipe(inout Parsed_packet headers,\ninout " + self.struct_name + " user_metadata,\ninout digest_data_t digest_data,\ninout sume_metadata_t sume_metadata) {\n" + _control_local_declarations.generate_code() + "\napply {\n" + table + ".apply();\n}\n}\n\n"
		scope.stop_local()
		code += "control TopDeparser(packet_out b, in Parsed_packet p, in " + self.struct_name + " user_metadata,\ninout digest_data_t digest_data,\ninout sume_metadata_t sume_metadata) {\napply {\n}\n}\n\n"
		return code

	def generate_random_controls(self):
		rnd = randomizer.randint(self.min_random_controls, self.max_random_controls)
		control_declarations = []
		for x in range(0, rnd):
			_control_declaration = control_declaration()
			_control_declaration.randomize()
			control_declarations.append(_control_declaration)
		code = ""
		for _control_declaration in control_declarations:
			code += _control_declaration.generate_code() + '\n\n'
		return code

	def generate_netfpga_init(self):
		code = "SimpleSumeSwitch(TopParser(),\nTopPipe(),\nTopDeparser()) main;"
		return code