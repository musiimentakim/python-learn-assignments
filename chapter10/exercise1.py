worddict = dict()
fhandle = input('Enter file name: ')
try:
    fhandle = open(fhandle)
except:
    print('cannot open file ',fhandle)

for line in fhandle:
    if  len(line) >= 2:
        if not line.startswith('From '):continue
        else:
            line = line.strip().split()
            word = line[1]
            worddict[word] = worddict.get(word,0) + 1
                
count_mail = list()
for key,value in list(worddict.items()):
    count_mail.append((value,key))
count_mail.sort(reverse = True)

for value,key in count_mail[:1]:
    print(key,value)

    
            
            

    
