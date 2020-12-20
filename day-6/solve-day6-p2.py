# Constants/Assumptions
formSeparator = ''

# Variable Initialization
strCurrForm = ''
sumYesAnswers = groupSize = i = 0

# Read Input File
with open('./input-day6') as inp:
	lines = [line.strip() for line in inp.readlines()]

# Lines loop
for i in range(len(lines)):
	strCurrForm += lines[i]
	groupSize += len(lines[i])>0 # Sum group elements

	if (lines[i] == formSeparator) | (i == len(lines) -1): # Keep appending until forms separator or EOF
		sCurrForm = set(strCurrForm) # Get Unique
		for j in sCurrForm: # Cycle unique yes answers
#			print strCurrForm + ':' + j + ' - ' +  str(strCurrForm.count(j))  + ':' + str(groupSize)
			if (strCurrForm.count(j) == groupSize): # All group elements answered yes 
				sumYesAnswers += 1
#				print 'Found: '+ j + ' : ' + strCurrForm + ' - Acumm: '+str(sumYesAnswers)
		strCurrForm = ''
		groupSize = 0

print 'Distinct Yes Answers: ' + str(sumYesAnswers)
