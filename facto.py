def facto(n):
    if n==0:
        return 1
    else:
        return n*facto(n-1)
k=int(input("ENTER AN INPUT")) 
print(facto(k))   
    
    

