class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # pass
        intervals.sort()
        p1=intervals[0][0]
        p2=intervals[0][1]
        ans=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=p2:
                p2=max(p2,intervals[i][1]) 
            else:
                if not ans:
                    ans.append([p1,p2])
                if ans and ans[-1]!=[p1,p2]:
                    ans.append([p1,p2])
                p1=intervals[i][0]
                p2=intervals[i][1]
        
        ans.append([p1,p2])
        return ans