
def minion_game(string):
    s=string.lower()
    n=len(s)
    o=['a','e','i','o','u']
    s=list(s)
    temp=n-1
    d=0
    kevin=0
    Stuart=0
    j=0
    for i in range(len(s)):
        if s[temp-i] in o:
            d=i+1
            kevin+=d
            print("kevin",end=' ')
            print(string,s[temp-i],kevin)
        else:
            j=i+1
            Stuart+=j
            print("Stuart",end=' ')
            print(string,s[temp-i],Stuart)
    if(kevin>Stuart):
        print("Kevin",kevin)
    elif(Stuart>kevin):
        print("Stuart",Stuart)
    else:
        print("Draw")                


minion_game("BANANA")
