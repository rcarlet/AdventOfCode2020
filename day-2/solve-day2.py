def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

with open('input-day2') as f:
	lines = f.readlines()

j=0
for i in range(len(lines)):
	min = lines[i].split('-')[0]
	max = lines[i].split('-')[1].split(' ')[0]
	needle = find_between(lines[i],' ',':')
	haystack = lines[i].split(' ')[2]
	print "Min="+str(min) + " " + "Max="+str(max) + " " + "Ndl="+str(needle) + " " + "Haystack="+haystack
#	print haystack.count(needle)
#	print haystack.count(needle)>=int(min)
#	print haystack.count(needle)<=int(max)
	if (haystack.count(needle)>=int(min)) and (haystack.count(needle)<=int(max)):
		print "Match: "+lines[i]
		j += 1
print "Total= "+str(j) 
	
