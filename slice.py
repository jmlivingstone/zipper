reader=open('test.txt','r')
count=0
for line in reader:
	tmp = line.strip()
	print len(tmp)
reader.close()

