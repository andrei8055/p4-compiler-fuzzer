import tempfile
import os
from targets.simple_switch import SimpleSwitch
from targets.fpga_switch import FpgaSwitch
import argparse

def main():
    # Parse the command line arguments provided at run time.
    parser = argparse.ArgumentParser(description="P4 Fuzzer Packet Tester")
    parser.add_argument(
        '-targ',
        '--target',
        dest='target',
        type=str,
        default='',
        help='The target: fpga or bmv')
    parser.add_argument(
        '-t',
        '--table',
        dest='table',
        type=str,
        default='',
        help='The table')
    parser.add_argument(
        '-a',
        '--action',
        dest='action',
        type=str,
        default='',
        help='The action')
    parser.add_argument(
        '-v',
        '--values',
        dest='values',
        nargs='+',
        help='<Required> Set flag',
        required=True)
    parser.add_argument(
        '-p',
        '--params',
        dest='params',
        nargs='+',
        default='',
        help='The parameters')
    parser.add_argument(
        '-pri',
        '--priority',
        dest='priority',
        type=int,
        default='',
        help='The priority')
    parser.add_argument(
        '-pkt',
        '--packets',
        dest='packets',
        nargs='+',
        default='',
        help='The packets')
    parser.add_argument(
        dest='input_file', type=str, help='Provide the path to the input file')

    # Parse the input arguments
    args = parser.parse_args()
    json_file = args.input_file
    table = args.table
    action = args.action
    priority = args.priority
    values = args.values
    params = args.params
    packets = args.packets

    # Start the --target switch and send the packets
    if args.target == 'fpga':
        print("running fpga_switch...")
        run_fpga_switch(args.input_file)
    else:
        print("running bmv_switch...")
        for packet in packets:
            run_bmw_switch(json_file, table, action, values, params, priority, packet)


def run_bmw_switch(input_file, table, action, values, params, priority, packet_data):
    tmpdir = tempfile.mkdtemp(dir=".")
    json_file = input_file

    #table add command in thrift
    # table_add IngressImpl.table0 IngressImpl.set_egress_port 0&&&511 0&&&281474976710655 0&&&281474976710655 0&&&65535 => 511 1
    # table, action, values[], params[], priority
    #switch.table_add("IngressImpl.table0", "IngressImpl.set_egress_port", ["0&&&511", "0&&&281474976710655", "0&&&281474976710655", "0&&&65535"], [0], 1)

    switch = SimpleSwitch(json_file, tmpdir)
    switch.table_add(table, action, values, params, priority)

    packet = bytearray(packet_data)
    switch.send_packet(packet)

    switch.clear_tables()
    switch.shutdown()
    # Don't remove "." !!!
    if tmpdir != ".":
        os.removedirs(tmpdir)


def run_fpga_switch(input_file, table, action, values, params, priority, packet_data):
    tmpdir = tempfile.mkdtemp(dir=".")
    json_file = input_file

    switch = FpgaSwitch(json_file, tmpdir)
    packet = bytearray(packet_data)

    switch.table_add(table, action, values, params, priority)
    switch.send_packet(packet)
    switch.clear_tables()
    switch.shutdown()

if __name__ == '__main__':
    main()
