with open('./input-day5') as inp:
	lines = [line.strip() for line in inp.readlines()]

maxSeatID = 0
for i in range(len(lines)):
	# Get Row
	rowBin = lines[i][:7].replace('B', '1').replace('F','0')
	rowInt = int(rowBin,2)

	# Get Column
	columnBin = lines[i][7:].replace('R', '1').replace('L','0')
	columnInt = int(columnBin,2)
	
	# Calculate Seat ID
	seatID = rowInt * 8 + columnInt

	# Get Max Seat ID	
	if seatID > maxSeatID:
		maxSeatID = seatID

print "Max Seat ID: "+str(maxSeatID)
