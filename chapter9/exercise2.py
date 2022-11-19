import string
day_dict = dict()
fhandle= ''

fhandle = input('Enter a file name: ')

if len(fhandle)> 0:
    try:
        fhandle = open(fhandle)
    except:
        print('cannot open file ',fhandle)
else:
    print('Enter file name to continue or exit to end program')
    
for line in fhandle :
    if  line.startswith('From ') :
        words = line.lower()
        words = line.translate(str.maketrans('','',string.punctuation))
        delimeter = ' '
        words = line.rstrip().split(delimeter)
        if len(words)> 3: 
            day = words[2]
            day_dict[day] = day_dict.get(day,0)+1
print(day_dict)
            
 
