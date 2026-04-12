class Solution(object):
    def sortPeople(self, names, heights):
        pairs = []

        for i in range(len(names)):
            pairs.append((heights[i], names[i]))

        pairs.sort(reverse=True)

        ans = []
        for h, name in pairs:
            ans.append(name)

        return ans