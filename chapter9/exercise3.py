word_dict = dict()
fhandle = input('Enter file name: ')

if len(fhandle)> 0:
    try:
        fhandle = open(fhandle)
        
        for line in fhandle:
            if not len(line) > 0 :continue
            
            else:
                if not line.startswith('From '):continue
                line = line.strip().split()
                words = line[1]
                word_dict[words] = word_dict.get(words,0) + 1
                
        print(word_dict)
        
    except:
        print('cannot open file ',fhandle)
else:       
    print('enter filename to proceed')

    
    






        
        
