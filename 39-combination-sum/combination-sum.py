class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        ds=[]
        a=self.find_combinations(0,candidates,target,ans,ds)
        return ans
    def find_combinations(self,index,candidates,target,ans,ds):
        if index==len(candidates):
            if target==0:
                ans.append(ds[:])

            return 
        if (candidates[index]<=target):
            ds.append(candidates[index])
            self.find_combinations(index,candidates,target-candidates[index],ans,ds)
            ds.pop()
        self.find_combinations(index+1,candidates,target,ans,ds)
        