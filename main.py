#!/usr/bin/python
import random
from derived_type import derived_type

#GENERATE HEADERS
derived_type = derived_type()

print '\n//generate random headers\n'
index = 0
header_number = 5
while index < header_number:
	print derived_type.get_header_type_declaration()
	index = index + 1


header_list = derived_type.get_header_list()

print '\n//generate header stacks\n'
for header in header_list:
	print derived_type.get_header_stack(header)

print '\n//generate header unions\n'
index = 0
header_union_number = 5
while index < header_union_number:
	header_union_members = random.randint(1, header_union_number)
	random_headers = random.sample(header_list, header_union_members)
	print derived_type.get_header_union_declaration(random_headers)
	index = index + 1




#GENERATE PARSERS

#GENERATE INGRESS PROCESSING

#GENERATE EGRESS PROCESSING

#GENERATE DEPARSERS
