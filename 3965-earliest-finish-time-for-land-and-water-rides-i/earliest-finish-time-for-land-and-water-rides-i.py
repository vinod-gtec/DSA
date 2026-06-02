class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        a=[]
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                landEnd=landStartTime[i]+landDuration[i]
                temp=max(landEnd,waterStartTime[j])+waterDuration[j]
                a.append(temp)
                waterEnd=waterStartTime[j]+waterDuration[j]
                temp=max(waterEnd,landStartTime[i])+landDuration[i]
                a.append(temp)
        a.sort()
        if len(a)>0:
            return a[0]
        return -1
        