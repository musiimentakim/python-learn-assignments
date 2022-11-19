word_dict = dict()
fhandle = input('enter file name: ')

if len(fhandle) > 0:
    try:
        fhandle = open(fhandle)

        for line in fhandle:
            if not line.startswith('From '):continue
            else:
                line = line.strip().lower()
                words = line.split()
                if len(words)>= 1:
                    word = words[1]
                    atpos = word.find('@')
                    word = word[atpos+1:]
                    word_dict[word] = word_dict.get(word,0)+1
                
        print(word_dict)
    except:
        print('cannot open file ',fhandle)
               
else:
    print('Enter file name to proceed')
