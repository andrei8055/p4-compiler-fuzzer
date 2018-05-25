import logging
import os
import subprocess
import sys
import time

from scapy.all import *


class FpgaSwitch:

    def __init__(self, json_file, folder, num_ports=8):
        pass

    def table_add(self, table, action, values, params, priority):
        pass

    def send_packet(self, packet):
        pass

    def clear_tables(self):
        pass

    def shutdown(self):
        pass