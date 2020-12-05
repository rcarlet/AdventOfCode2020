def findTree( stepR, stepD ):
	c = 0
	stepDown = stepD
	stepRight = stepR
	inputWidth = len(lines[0])
	for i in range(1,len(lines),stepDown):
        	pos = int(i*stepRight - round(i*stepRight/inputWidth)*inputWidth)
		print pos
        	content = lines[i][pos:pos+1]
	        print str(pos) + ": " + content
        	if content=="#":
                	c += 1
	return c

with open('input-day3-train') as f:
	lines = f.readlines()

#slopeOne = findTree(1,1)
#slopeTwo = findTree(3,1)
#slopeThree = findTree(5,1)
#slopeFour = findTree(7,1)
slopeFive = findTree(1,2)

#finalSlopes = slopeOne * slopeTwo * slopeThree * slopeFour * slopeFive

print "Total Trees: " + str(slopeFive)
