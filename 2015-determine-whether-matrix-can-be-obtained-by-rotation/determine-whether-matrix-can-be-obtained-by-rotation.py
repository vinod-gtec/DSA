class Solution(object):
    def rotate(self, mat):
        n = len(mat)

        # transpose
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # reverse rows
        for i in range(n):
            mat[i].reverse()

    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
        return False
        