sumvalue = 0
countvalue = 0

while True:
    try:
        line = input('enter a number :')
        if line == 'done':
            break
        else:
            line = int(line)
            sumvalue = sumvalue + line
            countvalue = countvalue + 1
            continue
    except:
        print('invalid input')
        continue
print('sum :', sumvalue)
print('count :', countvalue)
print('average :', sumvalue/countvalue )


        
