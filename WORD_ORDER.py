import collections
n=int(input())
ls=[]
for i in range(n):
    word=input()
    ls.append(word)
counter=collections.Counter(ls)
w=counter.values()
ls_set=set(ls)
print(len(ls_set))
for i in w:
    print(i,end=' ')
