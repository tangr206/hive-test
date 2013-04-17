#!/usr/bin/env python
import sys
import re
import time
for log in sys.stdin:
	line = log.strip()
	lin = line.split(" ")
	ipstr = lin[2]
	ipslit = ipstr.split(".")
	if len(ipslit) == 4:
		p = re.compile(r"([^=&?]+)=([^=&]+)")
		l = dict(filter(lambda t: t[0] in ['ref','sfet','fin','ff_id'], p.findall(line)))
		if len(l) == 4:
			x= lin[0] + "," + str(ipstr) + "," +  str(l['ref']) + "," + str(l['sfet']) + "," + str(l['fin']) + "," + str(l['ff_id']) + ",,,"
			print x
