class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        n=len(operations)
        a=[]
        counter=-1
        for i in range(n):
            if operations[i].isalpha():
                if operations[i]=="C":
                    if len(a)>0:
                        a.pop(counter)
                        counter=counter-1
                if operations[i]=="D":
                    temp=a[counter]*2
                    a.append(temp)
                    counter=counter+1
            elif operations[i]=="+":
                if counter>=1:
                    sum_temp=a[counter]+a[counter-1]
                    a.append(sum_temp)
                    counter=counter+1
            else:
                a.append(int(operations[i]))
                counter=counter+1
        final_val=0
        for i in a:
            final_val=final_val+i
        return final_val