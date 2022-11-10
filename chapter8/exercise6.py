num_list = []
while True:
    try:
        line = input('Enter a number: ')
        if line == 'done':
            break
        if len(line) <= 0:
            print('enter some data to compute ')
            continue
        line = float(line)
        num_list.append(line)
        continue
    except:
        print('enter numerical data')
        
if len(num_list)> 0:
    print('Maximum: ',max(num_list))
    print('Minumum: ',min(num_list))

else:
    print('list is empty,cannot compute maximum or minimum')
