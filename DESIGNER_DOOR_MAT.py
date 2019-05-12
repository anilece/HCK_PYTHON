
n, m = [int(x) for x in input(" first number(N) second number(3*N) :N must be odd :    ").split()] 
for i in range(1,n,2):
    j=1
    k=m-(3*i)
    while j<=(k//2):
        print("-",end="")
        j+=1
    f=1    
    while f<=i:
        print(".|.",end="")
        f+=1
    d=1
    while d<=k//2:
        print("-",end="")
        d=d+1
    print()
print("-"*((m-7)//2),"WELCOME","-"*((m-7)//2),sep="")
for i in range(1,(n//2+1)):
    j=1
    while j<=2*i+1*i:
        print("-",end="")
        j+=1
    w=1
    while w<=n-(2*i):
        print(".|.",end="")
        w+=1
    g=1
    while g<=2*i+1*i:
        print("-",end="")
        g+=1
    print()
    
     


