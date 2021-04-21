#!/usr/local/bin/python3

import sys

rosout = open(sys.argv[1], 'r')


lines = rosout.readlines()
total_delay = 0
count = 0

for i in range(0,len(lines),2):
	total_delay += int(lines[i].strip())
	count+=1

print(float(total_delay/count))


rosout.close()

