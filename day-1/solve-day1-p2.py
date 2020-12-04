with open('input-day1-p2') as f:
	lines = f.readlines()

for i in range(len(lines)):
	for j in range(len(lines)-1):
		for k in range(len(lines)-2):
			tot = int(lines[i])+int(lines[j])+int(lines[k])
			#print(tot)
			if tot == 2020:
				print "i="+str(i)+" j="+str(j)+": " + str(tot)+" k="+str(k)
				print lines[i] + " x " + lines[j] + " x " + lines[k] + " = " + str(int(lines[i])*int(lines[j])*int(lines[k]))
