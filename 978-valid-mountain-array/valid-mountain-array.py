class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count=0
        if len(arr)<=2:
            return False
        j=0
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                j=j+1
                pass
            else:
                count=count+1
                break
        for i in range(j,len(arr)-1):
            if arr[i]>arr[i+1]:
                pass
            else:
                count=count+1

        if count==1 and j>0:
            return True
        return False
