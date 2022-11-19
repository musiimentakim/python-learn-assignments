largest = 0
word_dict  = dict()
addresslist = list()

fhandle = input('Enter file name: ')

if len(fhandle) > 0 :
    try :
        fhandle = open(fhandle)
    except:
        print('cannot open file',fhandle)
        
    
    for line in fhandle:
        if not line.startswith('From '):continue
        else:
            line = line.strip().lower().split()
            
            if not len(line)>= 1: continue
            else:
                words = line[1]
                word_dict[words] = word_dict.get(words,0) + 1


    
    for key in word_dict:
        if largest == 0 or word_dict[key] > largest:                 
            largest = word_dict[key]
            if word_dict[key] == largest:
                address =(key,largest)

    addresslist.append(address)
    for key,value in addresslist:
        print(key,value)
                
else:
    print('enter file name to proceed')

            

    

