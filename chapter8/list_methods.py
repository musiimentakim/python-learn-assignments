numlist = []
while True:
    try:
        line = input('enter number to compute: ')
        numlist = numlist
        if len(line)>= 0:
            if line == 'done':break
            if line == 'clear':
                line1 = input('enter element to remove: ')
                line1 = str(line1)
                numlist.remove(line1)
            else :
                line = int(line)
                numlist.append(line)
                continue
            
        else:
            print('enter some data to compute')
    except:
        print('wrong data entered,expected integer')
print('sum: ',sum(numlist))
print('count: ',len(numlist))
try:
    print('average: ',sum(numlist)/len(numlist))
except:
    print('Oops average cannot be computed ,ensure to enter some data')
#print(numlist)            
