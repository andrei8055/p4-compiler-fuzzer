from struct_type_declaration import struct_type_declaration
from struct_field_list import struct_field_list
from scope import scope


class bmv2_random_program_generator(object):
	def __init__(self):
		pass

	def generate(self):
		scope.start_local()
		code = ""
		code += self.generate_bmv2_includes()
		code += self.generate_bmv2_structs()
		self.generate_random_structs()
		self.generate_random_headers()
		code += self.generate_bmv2_parser()
		self.generate_random_parsers()
		code += self.generate_bmv2_controls()
		self.generate_random_controls()
		code += self.generate_bmv2_init()
		return code

	def generate_bmv2_includes(self):
		# TODO: better
		return "#include <core.p4>\n#include <v1model.p4>\n"


	def generate_bmv2_structs(self):
		_struct_field_list = struct_field_list()
		_struct_field_list.randomize()
		headers_t = struct_type_declaration(name="headers_t", struct_field_list=_struct_field_list)
		_struct_field_list = struct_field_list()
		_struct_field_list.randomize()
		metadata_t = struct_type_declaration(name="metadata_t", struct_field_list=_struct_field_list)
		structs = (headers_t, metadata_t)
		code = ""
		for struct in structs:
			code += struct.generate_code()
		return code

	def generate_random_structs(self):
		pass

	def generate_random_headers(self):
		pass

	def generate_bmv2_parser(self):
		# TODO: Implement
		code = "parser ParserImpl(packet_in packet,\nout headers_t hdr,\ninout metadata_t meta,\ninout standard_metadata_t standard_metadata) {\nstate start {\ntransition select() {\n\ndefault: accept;\n}\n}\n}"
		return code

	def generate_random_parsers(self):
		pass

	def generate_bmv2_controls(self):
		# TODO: Implement
		code = "control IngressImpl(inout headers_t hdr,\ninout metadata_t meta,\ninout standard_metadata_t standard_metadata) {\napply {\n}\n}\n\n"
		code += "control EgressImpl(inout headers_t hdr,\ninout metadata_t meta,\ninout standard_metadata_t standard_metadata) {\napply {\n\n}\n}\n\n"
		code += "control VerifyChecksumImpl(inout headers_t hdr, inout metadata_t meta) {\napply {\n\n}\n}\n\n"
		code += "control ComputeChecksumImpl(inout headers_t hdr, inout metadata_t meta) {\napply {\n}\n}\n\n"
		code += "control DeparserImpl(packet_out packet, in headers_t hdr) {\napply {\n}\n}"
		return code

	def generate_random_controls(self):
		pass

	def generate_bmv2_init(self):
		# TODO: implement
		code = "V1Switch(ParserImpl(),\nVerifyChecksumImpl(),\nIngressImpl(),\nEgressImpl(),\nComputeChecksumImpl(),\nDeparserImpl()) main;"
		return code