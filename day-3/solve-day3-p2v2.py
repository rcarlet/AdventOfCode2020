def findTree( stepR, stepD ):
	x,y,c = 0,0,0
	while y < inputHeight-1:
		y += stepD
		x += stepR
		if lines[y][x%inputWidth] == '#':
			c += 1
#		print str(x)+":"+str(x%inputWidth)+":"+str(y)+":"+lines[y][x%inputWidth]
	return c

with open('./input-day3') as inp:
    lines = [line.strip() for line in inp.readlines()]

inputWidth = len(lines[0])
inputHeight = len(lines)

slopeOne = findTree(1,1)
slopeTwo = findTree(3,1)
slopeThree = findTree(5,1)
slopeFour = findTree(7,1)
slopeFive = findTree(1,2)

finalSlopes = slopeOne * slopeTwo * slopeThree * slopeFour * slopeFive

print "Total Trees: " + str(finalSlopes)
