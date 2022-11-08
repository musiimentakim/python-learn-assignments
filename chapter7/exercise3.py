
fhandle1 = input('Enter file name: ')
easter_egg = 'na na boo boo'
if  fhandle1 == easter_egg:
    print(easter_egg.upper(),'- You have been punk`d!')
    
else:
    try:
        fhandle = open(fhandle1 +'.txt')
        
        count = 0
        totalspam_confidence = 0
        for line in fhandle:
            if not line.startswith('X-DSPAM-Confidence:'):
                continue
            colon_pos = line.find(':')
            string_extract = line[colon_pos + 1 :]
            try:
                float_extract = float(string_extract.strip())
                count = count + 1
                totalspam_confidence = totalspam_confidence + float_extract
            except:
                print('data type conversion failed')
        print('averagespam_confidence: ',totalspam_confidence/count)
    except:
        print('cannot open file: ',fhandle1)
        

