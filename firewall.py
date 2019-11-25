import pandas as pd
import ipaddress

def split_port(range):
	start, end = \
		tuple(map(int, range.split('-')))
	return start, end

def split_ip(range):
	start, end = range.split('-')
	start = int(ipaddress.IPv4Address(start))
	end = int(ipaddress.IPv4Address(end))
	return start, end

class Firewall():

	def __init__(self, csv_file):
		self.db = dict()

		data = pd.read_csv(csv_file)

		# read the columns in the csv file called direction, protocol, port, and ip. Store as lists to parse through
		# Input files contain only valid entries, meaning don't have to check requirements
		direction = data.Direction.tolist()
		protocol = data.Protocol.tolist()
		port = data.Port.tolist()
		ip = data.IP.tolist()

		# direction, protocol, port and ip lists will all have same length of lists
		for d,pro,p,i in zip(direction,protocol,port,ip):
			# check if the database contains the current direction/protocol, if not initialize
			if d not in self.db:
				self.db[d] = {}
			a = self.db[d]
			if pro not in a:
				a[pro] = {}
			a = a[pro]
			# check if port/ip contains a range:
			if '-' in p:
				start_port, end_port = split_port(p)
			else:
				# save both start and end as port if it's not a range so that it can work for both cases
				start_port = p
				end_port = p
			start_port = int(start_port)
			end_port = int(end_port)

			if (start_port, end_port) not in a:
				a[(start_port, end_port)] = {}
			a = a[(start_port,end_port)]
			if '-' in i:
				start_ip, end_ip = split_ip(i)
			else:
				start_ip = int(ipaddress.IPv4Address(i))
				end_ip = int(ipaddress.IPv4Address(i))
			if (start_ip, end_ip) not in a:
				a[(start_ip,end_ip)] = {}



	def accept_packet(self,in_direction,in_protocol,in_port,in_ip) -> bool:
		# check against database
		db = self.db.get(in_direction)
		# if direction is not in db:
		if not db:
			return False
		db = db.get(in_protocol)
		if not db:
			return False
		for (start_port, end_port) in db.keys():
			if in_port >= start_port and in_port <= end_port:
				# check if its in the range at particular direction/protocol
				db = db[(start_port, end_port)]
				break
		else:
			return False
		ip_addr = int(ipaddress.IPv4Address(in_ip))
		for (start_ip, end_ip) in db.keys():
			if ip_addr >= start_ip and ip_addr <= end_ip:
				# the final value to check, can return true if it is reached (automatically break for loop)
				return True
		# otherwise ip address doesn't match ruleset from csv, return false
		return False