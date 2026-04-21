class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pb] = pa

        for a, b in allowedSwaps:
            union(a, b)

        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        ans = 0

        for g in groups.values():
            freq = {}

            for i in g:
                freq[source[i]] = freq.get(source[i], 0) + 1

            for i in g:
                if freq.get(target[i], 0) > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1

        return ans