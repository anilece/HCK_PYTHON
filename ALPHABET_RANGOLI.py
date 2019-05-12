def print_rangoli(size):
    n=size
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',           'w','x','y','z']
    for i in range(0,n):
            print((n-i-1)*2*'-',end='')
            k=0
            while k<=i:
                if (n-1-i+k)==n-1:
                    print(alp[n-1-k],end='')
                else:    
                    print(alp[n-1-k],end='')
                    print('-',end='')
                k+=1
            j=i
            while j>=1:
                    print('-',end='')        
                    print(alp[n-j],end='')
                    j-=1
            print((n-i-1)*2*'-',end='')        
            print()
    for i in range(1,n):
            print((i)*2*'-',end='')        
            k=n
            while k>i:
                print(alp[k-1],end='')
                if k>i+1:
                        print('-',end='')
                        k-=1
            k=n-1
            while k>i:
                print('-',end='')
                print(alp[n-k+i],end='')        
                k-=1
            print((i)*2*'-',end='')        
            print()

        
print_rangoli(6)
                
    

