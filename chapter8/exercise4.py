# still needs testing
unique_words =[]
fhandle = input('Enter file: ')
fhandle = open(fhandle)
for line in fhandle:
    words = line.rstrip().split()
    for word in words:
        if word in unique_words:continue
        unique_words.append(word)
newlist = unique_words[:]
newlist.sort()
print(newlist)
