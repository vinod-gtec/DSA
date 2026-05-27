class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        lower_last = {}
        upper_first = {}

        for i, ch in enumerate(word):

            if ch.islower():
                lower_last[ch] = i

            else:
                if ch not in upper_first:
                    upper_first[ch] = i

        count = 0

        for ch in lower_last:

            upper_ch = ch.upper()

            if upper_ch in upper_first:

                if lower_last[ch] < upper_first[upper_ch]:
                    count += 1

        return count