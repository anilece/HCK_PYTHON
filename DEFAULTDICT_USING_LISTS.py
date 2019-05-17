
n,m=map(int,input().split(" "))
first_list=[0]*n
second_list=[0]*m
for i in range(n):
    first_list[i]=input()
for j in range(m):
    second_list[j]=input()
for i in second_list:
    if i in first_list:
        for j in range(len(first_list)):
            if i==first_list[j]:
                print(j+1,end=' ')
        print()    
    else:
        print(-1)            
    
