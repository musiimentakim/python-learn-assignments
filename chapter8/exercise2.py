fhand = open('fail_file_construct.txt')
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3:continue
    
    else :
        if words[0] != 'From'  : continue
        print(words[2])

