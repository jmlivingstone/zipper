# display length of lines in file
import sys

for line in sys.stdin:
	tmp = line.strip()
	print len(tmp)

