def chop (t):
    x = t.remove(t[0]) 
    x = t.remove(t[len(t)-1])
    print(x)
    
        
def middle(t1):
    return t1[1:len(t1)-1]


# sample list
num1 = [2,3,4,6,5,8,10]

''' variable num1 and parameter t are aliases'''

# function calls
chop(num1)
print(num1)

t2 = middle(num1)
print(num1)

# verification 
print (t2 is num1)
    
