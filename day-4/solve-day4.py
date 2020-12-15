import re

passportSeparator = ''
rgxValidPassport = re.compile(r'\b(byr|iyr|eyr|hgt|hcl|ecl|pid)\b')

def linearizePassports( lines ):
	passports = []
	currPassport = ''
	for i in range(len(lines)):
        	currPassport += ' ' + lines[i]
        	if (lines[i] == passportSeparator) | (i == len(lines) -1): #Keep appending until passport separator or EOF
                	passports.append(currPassport)
                	currPassport = ''
	return passports


with open('./input-day4') as inp:
	lines = [line.strip() for line in inp.readlines()]

lnPassports = linearizePassports(lines)

validPassports = 0
for i in range(len(lnPassports)):
	if len(re.findall(rgxValidPassport,lnPassports[i])) == 7:
		validPassports += 1

print "Total Passports: "+str(len(lnPassports))
print "Valid Passports: "+str(validPassports)
