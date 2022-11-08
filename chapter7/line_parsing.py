fhandle = input('Enter file name: ')
try:
    fhandle = open(fhandle+'.txt')

    for line in fhandle:
        if not line.startswith('From '):continue
        words = line.lower().split()
        day = ['mon','tue','wed','thur','fri','sat','sun']
        for word in words:
            if word in day:
                print(word )
except:
    print('cannot open file ',fhandle)
    
