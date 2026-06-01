class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost=sorted(cost)
        amount=0
        counter=0
        for i in range(len(cost)-1,-1,-1):
            if counter<2:
                amount=amount+cost[i]
                counter=counter+1
            else:
                i=i-1
                counter=0
        return amount