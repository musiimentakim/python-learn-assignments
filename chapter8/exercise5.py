while True:
    fhandle = input('Enter a file name: ')
    try:
        fhandle = open(fhandle)
        word_list = []
        for line in fhandle:
            words = line.split()
            if len(words) < 2 or words[0] != 'From':continue
            print(words[1])
            word_list.append(words[1])
            
        print('There were ', len(word_list),' lines in the file with From as the first word')
                
    except:
        print('cannot open file',fhandle)
        
    
