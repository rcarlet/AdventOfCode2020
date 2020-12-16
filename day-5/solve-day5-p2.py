with open('./input-day5') as inp:
	lines = [line.strip() for line in inp.readlines()]

maxSeatID = 0
sumSeatID = 0
firstRow = int('0b0100000',2)

# Sum of initial n numbers (AP Sum)
idealSeatSum = 0

for i in range(len(lines)):
	# Get Row
	rowBin = lines[i][:7].replace('B', '1').replace('F','0')
	rowInt = int(rowBin,2)

	# Get Column
	columnBin = lines[i][7:].replace('R', '1').replace('L','0')
	columnInt = int(columnBin,2)

	# Get Seat ID
	seatID = rowInt * 8 + columnInt

        # Get Max Seat ID
        if seatID > maxSeatID:
                maxSeatID = seatID
	
	# Sum Seat IDs
	sumSeatID += seatID


# Sum of initial n numbers (AP Sum) - Removing very first
idealSeatSum = maxSeatID*(maxSeatID+1)/2 - (firstRow-1)*((firstRow-1)+1)/2

missingSeatID = idealSeatSum - sumSeatID 

print "Max Seat ID: " + str(maxSeatID)
print "My Seat: " + str(missingSeatID)
