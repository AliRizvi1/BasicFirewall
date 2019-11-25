from firewall import Firewall
import sys
from time import time as timer

if (len(sys.argv) == 1):
	print("Please include an input csv file as an argument")
	exit()
csv_file = sys.argv[1]

fw = Firewall(csv_file)
begTime = timer()
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))

# 5 test cases, elapsed time: 0.00011086463928222656 sec

elapsed_time = timer() - begTime
print("Elapsed time: ")
print(elapsed_time)