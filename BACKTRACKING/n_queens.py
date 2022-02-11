# global ans 
def isSafe(arr,r,c):
    #colwise
    # print('----------',r,c)
    i = r-1
    while i>=0:
        if arr[i][c]:
            return False
        i-=1
    # for i in range(n):
        # if arr[i][c]:
            # return False
    #diagonal left
    i,j=r,c
    while i>=0 and j>=0:
        # print(i,j)
        if arr[i][j]:
            return False
        i-=1
        j-=1
        # i-=1
    #diagonal right:
    i,j=r,c
    while i>=0 and j<len(arr):
        if arr[i][j]:
            return False
        i-=1
        j+=1
    return True
def nQueen(arr,row,col,path):
    print('row',row)
    print('path',path)
    if row==len(arr):
        print('------------------',arr)
        print(path)
        return 
    for i in range(len(arr[0])):
        # print(isSafe(arr,row,col))
        if(isSafe(arr,row,i)):
            arr[row][i] = 1
            nQueen(arr,row+1,i,path+str(row)+'|'+str(i)+',')
            arr[row][i] = 0



n=int(input())
arr=[]
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(0)
    arr.append(tmp)
print(arr)
print(nQueen(arr,0,0,''))