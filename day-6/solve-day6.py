with open('./input-day6') as inp:
	lines = [line.strip() for line in inp.readlines()]

formSeparator = ''

currForm = ''
sumYesAnswers = 0

for i in range(len(lines)):
	currForm += lines[i]
	if (lines[i] == formSeparator) | (i == len(lines) -1): #Keep appending until forms separator or EOF
		sumYesAnswers += len(set(currForm))
		currForm = ''

print 'Distinct Yes Answers: ' + str(sumYesAnswers)
