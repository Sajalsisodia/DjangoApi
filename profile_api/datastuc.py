for i in range(1,7):
    for k in range(1,7-i):
        print(" ",end="")
        
    for j in range(1,i+1):
        print("* ",end="")
        
    print()
    
    
for i in range(7,1,-1):
    for k in range(i,7):
        print(" ",end="")
        
    for j in range(1,i+1):
        print("* ",end="")
        
    print()