num_list = []
while True:
    try:
        line = input('Enter number: ')
        if line == 'done':
            break
        else:
            line = int(line)
            num_list.append(line)
            continue
    except:
        print('invalid input')
        continue
print('minimum value :', min(num_list))
print('maximum value :', max(num_list))
