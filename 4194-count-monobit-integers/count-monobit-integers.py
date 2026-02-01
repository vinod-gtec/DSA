class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]
        if n==0:
            return 1
        if n==1:
            return 2

        for i in range(1, n + 1):
            num = 0
            place = 1
            x = i
            while x > 0:
                num += (x % 2) * place
                place *= 10
                x //= 2
            res.append(num)

        a=[]
        for i in res:
            a.append(str(i))
        b=[]
        count=0
        for i in range(len(a)):
            is_mono=True
            for j in range(len(a[i])):
                if(a[i][j]!=a[i][0]):
                    is_mono=False                
                    break
            if is_mono:
                count=count+1

        return count


            
