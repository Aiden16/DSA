def PalinArray(arr ,n):
    # Code here
    
    for i in arr:
        t = i
        res = 0
        while t>0:
            last = t%10
            res = 10*res+last
            t=t//10
        if res!=i:
            return 0
    return 1