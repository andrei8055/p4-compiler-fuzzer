#!/usr/bin/python
import sys
from base_type_generator import base_type_generator
from derived_type import derived_type
from enum_generator import enum_generator
from header_generator import header_generator
from header_union_generator import header_union_generator
from header_stack_generator import header_stack_generator
from struct_generator import struct_generator
from tuple_generator import tuple_generator
from include_generator import include_generator
from annotation_generator import annotation_generator
from parser_generator import parser_generator
from state_generator import state_generator
from control_generator import control_generator
from common import common

filename = ""
console = True

if len(sys.argv) > 1:
	filename = sys.argv[1]
	if(sys.argv[2] == ""):
		console = False
	else:
		console = True
else:
	sys.exit("Error! Missing argument 1 - output filename")

# print the program to file
file = open(filename, "w")

common = common()

#generate includes
include_generator = include_generator()


include_corep4 = include_generator.generate("core.p4")
include_v1modelp4 = include_generator.generate("v1model.p4")

common.output(include_generator.generate_code(include_corep4), console, file)
common.output(include_generator.generate_code(include_v1modelp4), console, file)

#generate headers
header_generator = header_generator()
annotation_generator = annotation_generator()
base_type_generator = base_type_generator()

#---ethernet header---
dst_addr_field = base_type_generator.generate_base_type("dst_addr", 48, "bit")
src_addr_field = base_type_generator.generate_base_type("src_addr", 48, "bit")
ether_type_field = base_type_generator.generate_base_type("ether_type", 16, "bit")
ethernet_t_header = header_generator.generate("ethernet_t", [dst_addr_field, src_addr_field, ether_type_field])
common.output(header_generator.generate_code(ethernet_t_header), console, file)

#---ipv4 header---
version_field = base_type_generator.generate_base_type("version", 4, "bit")
ihl_field = base_type_generator.generate_base_type("ihl", 4, "bit")
diffserv_field = base_type_generator.generate_base_type("diffserv", 8, "bit")
len_field = base_type_generator.generate_base_type("len", 16, "bit")
identification_field = base_type_generator.generate_base_type("identification", 16, "bit")
flags_field = base_type_generator.generate_base_type("flags", 3, "bit")
frag_offset_field = base_type_generator.generate_base_type("frag_offset", 13, "bit")
ttl_field = base_type_generator.generate_base_type("ttl", 8, "bit")
protocol_field = base_type_generator.generate_base_type("protocol", 8, "bit")
hdr_checksum_field = base_type_generator.generate_base_type("hdr_checksum", 16, "bit")
src_addr_field = base_type_generator.generate_base_type("src_addr", 32, "bit")
dst_addr_field = base_type_generator.generate_base_type("dst_addr", 32, "bit")
ipv4_t_header = header_generator.generate("ipv4_t", [version_field, ihl_field, diffserv_field, len_field,
													 identification_field, flags_field, frag_offset_field, ttl_field,
													 protocol_field, hdr_checksum_field, src_addr_field, dst_addr_field])
common.output(header_generator.generate_code(ipv4_t_header), console, file)


#---packet in header---
packet_in_annotation = annotation_generator.generate("controller_header", "packet_in")
ingress_port_field = base_type_generator.generate_base_type("ingress_port", 9, "bit")
packet_in_header_t_header = header_generator.generate("packet_in_header_t", [ingress_port_field])
common.output(annotation_generator.generate_code(packet_in_annotation), console, file)
common.output(header_generator.generate_code(packet_in_header_t_header), console, file)

#---packet out header---
packet_out_annotation = annotation_generator.generate("controller_header", "packet_out")
egress_port_field = base_type_generator.generate_base_type("egress_port", 9, "bit")
packet_out_header_t_header = header_generator.generate("packet_out_header_t", [ingress_port_field])
common.output(annotation_generator.generate_code(packet_out_annotation), console, file)
common.output(header_generator.generate_code(packet_out_header_t_header), console, file)

#generate structs
struct_generator = struct_generator()

#---headers struct---
ethernet_field = derived_type("ethernet", ethernet_t_header, ethernet_t_header.get_name(),
							  ethernet_t_header.get_base_type())
ipv4_field = derived_type("ipv4", ipv4_t_header, ipv4_t_header.get_name(), ipv4_t_header.get_base_type())
packet_in_field = derived_type("packet_in", packet_in_header_t_header, packet_in_header_t_header.get_name(),
							   packet_in_header_t_header.get_base_type())
packet_out_field = derived_type("packet_out", packet_out_header_t_header, packet_out_header_t_header.get_name(),
								packet_out_header_t_header.get_base_type())
headers_t_struct = struct_generator.generate("headers_t", [ethernet_field, ipv4_field,
														  packet_in_field, packet_out_field])
common.output(struct_generator.generate_code(headers_t_struct), console, file)

#---metadata struct---
metadata_t_struct = struct_generator.generate("metadata_t", [])
common.output(struct_generator.generate_code(metadata_t_struct), console, file)

# GENERATE PARSERS
parser_generator = parser_generator()
state_generator = state_generator()
start_state = state_generator.generate("start", "transition select(standard_metadata.ingress_port) { \n default: accept;} \n")
test_parser = parser_generator.generate("ParserImpl", ["packet_in packet", "out headers_t hdr", "inout metadata_t meta",
													   "inout standard_metadata_t standard_metadata"], [start_state])
common.output(parser_generator.generate_code(test_parser), console, file)


#GENERATE CONTROLS
control_generator = control_generator()

#--- verify checksum control---
verify_checksum_impl_control = control_generator.generate("VerifyChecksumImpl", ["inout headers_t hdr",
																				 "inout metadata_t meta"],
														  "apply {}")
common.output(control_generator.generate_code(verify_checksum_impl_control), console, file)

#--- compute checksum control---
compute_checksum_impl_control = control_generator.generate("ComputeChecksumImpl", ["inout headers_t hdr", "inout metadata_t meta"],
														  "apply {}")
common.output(control_generator.generate_code(compute_checksum_impl_control), console, file)

#--- ingress control---
ingress_impl_control = control_generator.generate("IngressImpl", ["inout headers_t hdr", "inout metadata_t meta",
																  "inout standard_metadata_t standard_metadata"],
														  "action _drop () { } \n apply { } \n")
common.output(control_generator.generate_code(ingress_impl_control), console, file)

#--- egress control---
egress_impl_control = control_generator.generate("EgressImpl", ["inout headers_t hdr", "inout metadata_t meta",
																"inout standard_metadata_t standard_metadata"],
														  "apply{} \n")
common.output(control_generator.generate_code(egress_impl_control), console, file)

#--- deparser control---
deparser_impl_control = control_generator.generate("DeparserImpl", ["packet_out packet", "in headers_t hdr"], "apply {}")
common.output(control_generator.generate_code(deparser_impl_control), console, file)


# GENERATE SWITCH INSTANTIONATION
code = ''

code = 'V1Switch(ParserImpl(), \n'
code = code + 'VerifyChecksumImpl(), \n'
code = code + 'IngressImpl(), \n'
code = code + 'EgressImpl(), \n'
code = code + 'ComputeChecksumImpl(), \n'
code = code + 'DeparserImpl()) main; \n'
code = code + ' \n'

common.output(code, console, file)