fhandle = input('Enter file name: ')
try:
    fhandle = open(fhandle+'.txt')

    totalspam_confidence = 0
    count = 0
    for line in fhandle:
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        colon_pos = line.find(':')
        
        #line slicing
        string_extract = line[colon_pos + 1 :]
        
        try:
            float_extract = float(string_extract.strip())
        except:
            print('data type conversion failed')
            
        totalspam_confidence = totalspam_confidence + float_extract
        count = count + 1

    print('average spam confidence :',totalspam_confidence/count)
    
    
except:
    print('failed to open file: ',fhandle)
    
    
        
            
