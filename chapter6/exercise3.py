def count (string,letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    print('lettercount :',count)
   

stringinput = input('Enter string :')
letterinput = input('Enter letter :')

#function call takes on input variable arguments
count(stringinput,letterinput)
                
