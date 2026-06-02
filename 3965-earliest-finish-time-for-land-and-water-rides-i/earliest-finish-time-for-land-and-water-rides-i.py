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
        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                waterEnd=waterStartTime[i]+waterDuration[i]
                temp=max(waterEnd,landStartTime[j])+landDuration[j]
                a.append(temp)
        a.sort()
        if len(a)>0:
            return a[0]
        return -1
        