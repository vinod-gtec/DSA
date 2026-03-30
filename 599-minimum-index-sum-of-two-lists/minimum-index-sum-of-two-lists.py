class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        
        # Store index of each restaurant in list1
        for i in range(len(list1)):
            d[list1[i]] = i
        
        res = []
        min_sum = float('inf')
        
        # Traverse list2
        for j in range(len(list2)):
            if list2[j] in d:
                total = j + d[list2[j]]
                
                if total < min_sum:
                    min_sum = total
                    res = [list2[j]]   # reset list
                
                elif total == min_sum:
                    res.append(list2[j])
        
        return res
        