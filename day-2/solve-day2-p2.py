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
	pos1 = int(lines[i].split('-')[0])
	pos2 = int(lines[i].split('-')[1].split(' ')[0])
	needle = find_between(lines[i],' ',':')
	haystack = lines[i].split(' ')[2]
	print "Pos 1="+str(pos1) + " " + "Pos 2="+str(pos2) + " " + "Ndl="+str(needle) + " " + "Haystack="+haystack
#	print haystack.count(needle)
#	print haystack.count(needle)>=int(min)
#	print haystack.count(needle)<=int(max)
	
	
	if (len(haystack)>pos1-1 and len(haystack)>pos2-1) and (haystack[pos1-1]==needle) and (haystack[pos2-1]!=needle):
		print "Match 1: "+lines[i]
		j += 1

        if (len(haystack)>pos1-1 and len(haystack)>pos2-1) and (haystack[pos1-1]!=needle) and (haystack[pos2-1]==needle):
                print "Match 2: "+lines[i]
                j += 1

print "Total= "+str(j) 
	
