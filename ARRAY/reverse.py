
def reverseWord(s):
    #your code here
    s=list(s)
    p1,p2=0,len(s)-1
    # print(p1,p2,len(s)-1)
    while p1<=p2:
        s[p1],s[p2] = s[p2],s[p1]
        # print(s)
        p1+=1
        p2-=1
        # print(p1,p2)
    return ''.join(s)