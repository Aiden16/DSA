def soln(nums):

    arr = []
    for ind,val in enumerate(nums):
        arr.append([val,ind])
    arr.sort(key=lambda k:k[0])
    new_arr = [val for ind,val in arr]
    print(new_arr)
    # arr[0],arr[1] = arr[1],arr[0]
    swaps = 0
    i = 0
    while i<len(new_arr):
        # print(i,arr[i][1],arr[arr[i][1]],arr[i])
        # i+=1
        if i<len(new_arr):
            # print(new_arr[i],new_arr[new_arr[i][1]],i,new_arr[i][1])
            # tmp = new_arr[i]
            print(new_arr[i],new_arr[new_arr[i]])
            ind = new_arr[i]
            new_arr[i],new_arr[ind] = new_arr[ind],new_arr[i]
            # new_arr[i] = new_arr[2]
            # new_arr[2] = tmp
            print(new_arr)
            # i-=1
        i+=1
nums = list(map(int,input().split(' ')))
soln(nums)