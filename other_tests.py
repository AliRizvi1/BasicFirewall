from firewall import Firewall
import sys
from time import time as timer

if (len(sys.argv) == 1):
	print("Please include an input csv file as an argument")
	exit()
csv_file = sys.argv[1]

fw = Firewall(csv_file)
begTime = timer()
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(fw.accept_packet("inbound", "tcp", 53, "192.168.2.1"))
print(fw.accept_packet("outbound", "tcp", 20000, "192.168.10.11"))
print(fw.accept_packet("outbound","udp",1021,"52.12.48.92"))

for i in range(1,500000):
	# 500004 test cases, elapsed time: 17.200738191604614 sec
	print(fw.accept_packet("inbound", "tcp", i, "192.168.1.1"))

# print time:
elapsed_time = timer() - begTime
print("Elapsed time: ")
print(elapsed_time)