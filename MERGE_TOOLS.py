def merge_the_tools(string, k):
    s=string
    d=[]
    j=0
    for i in range(0,len(s),k):
        j=i
        e=''
        o=0
        while o<k:
            e+=s[j]
            j+=1
            o+=1
        d.append(e)
    for i in range(len(d)):
        r=d[i]
        r=list(r)
        for i in range(len(r)):
            j=len(r)-1
            while j>0:
                if r[i]==r[j] and i!=j:
                    r[j]=' '
                j-=1
        for i in (r):
            if i!=" "and i  in r:
                print(i,end='')
        print()

merge_the_tools("AABCAAADA",3)        
