class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        used=[False]*len(nums)
        self.combinations(nums,used,[],ans)
        return ans
        
    def combinations(self,nums,used,current,ans):
        if len(current)==len(nums):
            ans.append(current[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            self.combinations(nums, used, current, ans)

            # Backtrack: remove element and mark unused
            current.pop()
            used[i] = False
        return ans

        