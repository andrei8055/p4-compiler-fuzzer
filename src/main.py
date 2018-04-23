from base_type_generator import base_type_generator
from parser_generator import parser_generator
from include import include
from state_generator import state_generator
from expression_generator import expression_generator
from declaration_generator import declaration_generator
from annotation import annotation
from bit import bit
from constant import constant
from parameter import parameter
from control import control
from header import header
from struct_field import struct_field
from action import action
from table import table
from table_actions import table_actions
from table_default_action import table_default_action
from header_union import header_union
from struct import struct
from enumeration import enumeration
from tuple import tuple
from bool import bool

import sys
import os
import random
from common import common

filename = ""
console = False

if len(sys.argv) > 1:
	filename = sys.argv[1]
	if(sys.argv[2] == "false"):
		console = False
	else:
		console = True
else:
	sys.exit("Error! Missing argument 1 - output filename")

# print the program to file
curdir = os.path.dirname(__file__)
file_path = os.path.join(curdir, filename)
file = open(file_path, "w")

#generators objects
common = common()
base_type_generator = base_type_generator()
expression_generator = expression_generator()
declaration_generator = declaration_generator()

#generate includes
include_corep4 = include("core.p4")
include_v1modelp4 = include("v1model.p4")

common.output(include_corep4.generate_code(), console, file)
common.output(include_v1modelp4.generate_code(), console, file)
#---fuzzing section---


random_base_types = []
random_headers = []
random_enums = []
random_structs = []
random_header_stacks = []
random_header_unions = []

for x in range(0, random.randint(1, 20)):
	rbt = base_type_generator.generate_random(['bit', 'bool', 'varbit', 'int'])
	random_base_types.append(rbt)

for x in range(2, random.randint(2, 20)):
	rh = header()
	rh.randomize()
	random_headers.append(rh)
	common.output(rh.generate_code(), console, file)

for x in range(1, random.randint(1, 20)):
	re = enumeration()
	re.randomize()
	random_enums.append(re)
	common.output(re.generate_code(), console, file)

for y in range(0, random.randint(1, 10)):
	rhu = header_union()
	rhu.randomize(random_headers)
	common.output(rhu.generate_code(), console, file)
	random_header_unions.append(rhu)

for x in range(1, random.randint(1, 20)):
	all_types = random_base_types + random_structs + random_enums + random_headers + random_header_unions
	rs = struct()
	rs.randomize(all_types)
	random_structs.append(rs)
	common.output(rs.generate_code(), console, file)

#generate headers
#---ethernet header---
dst_addr_field = struct_field(annotation(), bit(48), "dst_addr")
src_addr_field = struct_field(annotation(), bit(48), "src_addr")
ether_type_field = struct_field(annotation(), bit(16), "ether_type")

ethernet_t_header = header(annotation(), "ethernet_t", [dst_addr_field, src_addr_field, ether_type_field])
common.output(ethernet_t_header.generate_code(), console, file)

#---ipv4 header---
version_field = struct_field(annotation(), bit(4), "version")
ihl_field = struct_field(annotation(), bit(4), "ihl")
diffserv_field = struct_field(annotation(), bit(8), "diffserv")
len_field = struct_field(annotation(), bit(16), "len")
identification_field = struct_field(annotation(), bit(16), "identification")
flags_field = struct_field(annotation(), bit(3), "flags")
frag_offset_field = struct_field(annotation(), bit(13), "frag_offset")
ttl_field = struct_field(annotation(), bit(8), "ttl")
protocol_field = struct_field(annotation(), bit(8), "protocol")
hdr_checksum_field = struct_field(annotation(), bit(16), "hdr_checksum")
src_addr_field = struct_field(annotation(), bit(32), "src_addr")
dst_addr_field = struct_field(annotation(), bit(32), "dst_addr")

ipv4_t_header = header(annotation(), "ipv4_t", [version_field, ihl_field, diffserv_field, len_field,
													 identification_field, flags_field, frag_offset_field, ttl_field,
													 protocol_field, hdr_checksum_field, src_addr_field, dst_addr_field])
common.output(ipv4_t_header.generate_code(), console, file)


#---packet in header---
packet_in_annotation = annotation("controller_header", ["packet_in"])
ingress_port_field = struct_field(annotation(), bit(9), "ingress_port")
packet_in_header_t_header = header(packet_in_annotation, "packet_in_header_t", [ingress_port_field])

common.output(packet_in_header_t_header.generate_code(), console, file)

#---packet out header---
packet_out_annotation = annotation("controller_header", ["packet_out"])
egress_port_field = struct_field(annotation(), bit(9), "egress_port")
packet_out_header_t_header = header(packet_out_annotation, "packet_out_header_t", [ingress_port_field])

common.output(packet_out_header_t_header.generate_code(), console, file)

#generate structs


#---headers struct---
headers_t_struct = struct(annotation(), "headers_t", [ethernet_t_header, ipv4_t_header, packet_in_header_t_header, packet_out_header_t_header])
common.output(headers_t_struct.generate_code(), console, file)

#---metadata struct---
metadata_t_struct = struct(annotation(), "metadata_t", [])
common.output(metadata_t_struct.generate_code(), console, file)

# GENERATE PARSERS
parser_generator = parser_generator()
state_generator = state_generator()

_constant = constant()
_constant.randomize()

start_state = state_generator.generate("start", "transition select(standard_metadata.ingress_port) { \n default: accept;} \n")

param_1 = parameter("", "packet_in", "packet")
param_2 = parameter("out", "headers_t", "hdr")
param_3 = parameter("inout", "metadata_t", "meta")
param_4 = parameter("inout", "standard_metadata_t", "standard_metadata")

test_parser = parser_generator.generate("ParserImpl", [param_1, param_2, param_3, param_4], [_constant], [], [start_state])
common.output(parser_generator.generate_code(test_parser), console, file)


#GENERATE CONTROLS
x_parameter = parameter("inout", "bit<32>", "x")
#action_declaration = declaration_generator.generate_action("a", ["inout bit<32> b", "bit<32> d"], "b = d;")
action_declaration = action(annotation(), "a", [parameter("inout", "bit<32>", "b"), parameter("", "bit<32>", "d")])

_table_actions = table_actions({action_declaration: ["x"]})
_default_action = table_default_action(action_declaration.generate_code_ref(["x", "0"]))

property_list = [_table_actions, _default_action]
table_declaration = table(annotation(), "t", property_list)
apply_declaration = declaration_generator.generate_apply("t.apply();")

test_control = control(annotation(), "c", [], [x_parameter], [action_declaration, table_declaration], "apply { t.apply(); }")
common.output(test_control.generate_code(), console, file)

#--- verify checksum control---

hdr_parameter = parameter("inout", "headers_t", "hdr")
meta_parameter = parameter("inout", "metadata_t", "meta")
standard_metadata = parameter("inout", "standard_metadata_t", "standard_metadata")
verify_checksum_impl_control = control(annotation(), "VerifyChecksumImpl", [], [hdr_parameter, meta_parameter], [], "apply {}")
common.output(verify_checksum_impl_control.generate_code(), console, file)

#--- compute checksum control---
compute_checksum_impl_control = control(annotation(), "ComputeChecksumImpl", [],  [hdr_parameter, meta_parameter], [], "apply {}")
common.output(compute_checksum_impl_control.generate_code(), console, file)

#--- ingress control---
ingress_impl_control = control(annotation(), "IngressImpl", [], [hdr_parameter, meta_parameter, standard_metadata], [], "apply {}")
common.output(ingress_impl_control.generate_code(), console, file)

#--- egress control---
egress_impl_control = control(annotation(), "EgressImpl", [], [hdr_parameter, meta_parameter, standard_metadata], [], "apply{}")
common.output(egress_impl_control.generate_code(), console, file)

#--- deparser control---
packet_parameter = parameter("", "packet_out", "packet")
hdr_parameter = parameter("in", "headers_t", "hdr")
deparser_impl_control = control(annotation(), "DeparserImpl", [], [packet_parameter, hdr_parameter], [], "apply {}")
common.output(deparser_impl_control.generate_code(), console, file)


# GENERATE SWITCH INSTANTIONATION
code = 'V1Switch(ParserImpl(), \n'
code = code + 'VerifyChecksumImpl(), \n'
code = code + 'IngressImpl(), \n'
code = code + 'EgressImpl(), \n'
code = code + 'ComputeChecksumImpl(), \n'
code = code + 'DeparserImpl()) main; \n'
code = code + ' \n'

common.output(code, console, file)