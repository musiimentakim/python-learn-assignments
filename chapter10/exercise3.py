
#need to remove integers
import string
letterdict =  dict()
fhandle = input('Enter file name: ')
try:
    fhandle = open(fhandle)
except:
    print('cannot open file',fhandle)

for line in fhandle:
    # removing punctuations
    line = line.translate(str.maketrans('','',string.punctuation))
    # removing digits
    line = line.translate(str.maketrans('','',string.digits))
    line = line.lower().split()
    for word in line:
        word = word.strip()
        for letter in word:
            letterdict[letter] = letterdict.get(letter,0)+ 1
letterlist = list()
for key,value in list(letterdict.items()):
    letterlist.append((value,key))
    letterlist.sort(reverse = True)
for count,letter in letterlist:
    print(letter,count)
    
