# using try and except
try:
    hours = input('Enter hours : ')
    hours = float(hours)
    rate = input('Enter rate : ')
    rate = float(rate)
    
    if hours < 40 :
        pay = rate * hours
        print('Pay :',str(pay))
    else:
        pay = (40 * rate) +(( hours - 40) * rate *1.5)
        print('Pay :',str(pay))
        
except:
    if type(hours) != float: 
        print('enter numerical data')
    elif type(rate) != float:
        print('enter numerical data')
        

