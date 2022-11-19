fhandle = input('enter file name: ')
word_dic = dict()
try:
    fhandle = open(fhandle)
except:
    print('cannot open file', fhandle)
    
for line in fhandle:
    words = line.rstrip().split()
    for word in words :
        word_dic[word]='characters'

word_list = list(word_dic.values())
x = 'characters' in word_list
print(x)

    

    
    
