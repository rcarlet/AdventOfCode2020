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
		iPassport = dict(s.split(':', 1) for s in lnPassports[i].split())

		vld_byr = vld_iyr = vld_eyr = vld_hgt = vld_hcl = vld_ecl = vld_pid = False
		#Birth Year 1920 <= byr <= 2002
		vld_byr = (int(iPassport['byr']) >= 1920) & (int(iPassport['byr']) <= 2002)

		#Issue Year 2010 <= iyr <= 2020
		vld_iyr = (int(iPassport['iyr']) >= 2010) & (int(iPassport['iyr']) <= 2020)

		#Expiration Year 2020 <= eyr <= 2030
		vld_eyr = (int(iPassport['eyr']) >= 2020) & (int(iPassport['eyr']) <= 2030)

		#Height
		idHgtInUnit = iPassport['hgt'].find('in')
		idHgtCmUnit = iPassport['hgt'].find('cm')
		if (idHgtInUnit != -1):
			hgt = iPassport['hgt'][:idHgtInUnit]
			vld_hgt = (int(hgt) >= 59) & (int(hgt) <= 76)
		if (idHgtCmUnit != -1):
			hgt = iPassport['hgt'][:idHgtCmUnit]
			vld_hgt = (int(hgt) >= 150) & (int(hgt) <= 193)

		#Hair Color
		rgxValidHairColor = re.compile(r'#[0-9a-f]{6}$')
		vld_hcl = bool(rgxValidHairColor.match(iPassport['hcl']))		

		#Eye Color
		validEyeColors = ['amb','blu','brn','gry','grn','hzl','oth']
		vld_ecl = any(substring in iPassport['ecl'] for substring in validEyeColors)

		#Passport ID
		rgxValidPID = re.compile(r'[0-9]{9}$')
		vld_pid = bool(rgxValidPID.match(iPassport['pid']))
		
		if (vld_byr & vld_iyr & vld_eyr & vld_hgt & vld_hcl & vld_ecl & vld_pid):
			validPassports += 1

print "Total Passports: "+str(len(lnPassports))
print "Valid Passports: "+str(validPassports)
