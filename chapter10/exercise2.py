
hourdict = dict()
fhandle = input('Enter file name: ')
try:
    fhandle = open(fhandle)
except:
    print('cannot open file ',fhandle)
    
for line in fhandle:
    if len(line)> 0:
        if not line.startswith('From'):continue
        else:
            line = line.strip().split()
            if len(line)>= 6:
                word = line[-2]
                delimeter = ':'
                hour,minute,second = word.split(delimeter)
                hourdict[hour] = hourdict.get(hour,0) + 1

hourlist = list()
for hour,hourcount in list(hourdict.items()):
    hourlist.append((hour,hourcount))
    hourlist.sort()
    
for hour , hourcount in hourlist:
    print(hour,hourcount)

            
            
