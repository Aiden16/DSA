class Solution:
    def sort012(self,array,n):
        #o(n)
        #dutch national flag algorithm
        zero,one,two=0,0,len(array)-1
        while one<=two:
            if array[one] == 0:
                array[zero],array[one] = array[one],array[zero]
                zero+=1
                one+=1
            elif array[one] == 1:
                one+=1
            elif array[one] == 2:
                array[one],array[two] = array[two],array[one]
                two-=1
        return array