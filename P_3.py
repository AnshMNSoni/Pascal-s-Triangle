# Pascal's Triangle:

n = int(input("Enter the number of rows you want in Pascal's Triangle: "))

# to print 1 ::
print((n)*' ', ' 1', '\n')  

# to print 1 1 ::  
print((n)*' ', '1 1', '\n')         

# to print rest ::
l2 = [1, 1]

for i in range (3, n + 1):          
    
    # Starting from 3 because -> Already 2 lines are used above
    # So, as to maintain the order +3 is added at all numeric sections
    
    print((n - i + 3)*' ', end = '')

    l1 = [1, 1]
    
    for j in range (3, i + 1):
        value = l2[j - 3] + l2[j - 2]
        l1.insert(j - 2, value)
        
    for k in l1:
        print(k, end = ' ')
    
    print('\n')
    
    l2 = l1