with open('input-day3') as f:
	lines = f.readlines()

c=0
for i in range(len(lines)):
	pos = int(i*3 - round(i*3/31)*31)
	content = lines[i][pos:pos+1]
#	print str(pos) + ": " + content
	if content=="#":
		c += 1
print "Total Trees: " + str(c)
