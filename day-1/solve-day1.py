with open('input-day1') as f:
	lines = f.readlines()

for i in range(len(lines)):
	for j in range(len(lines)-1):
		tot = int(lines[i])+int(lines[j])
		if tot == 2020:
			print "i="+str(i)+" j="+str(j)+": " + str(tot)
			print lines[i] + " x " + lines[j] + " = " + str(int(lines[i])*int(lines[j]))
