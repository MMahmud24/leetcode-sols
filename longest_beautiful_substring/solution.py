class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        l = 0
        n = len(word)
        max_length = 0
        counts = 1
        for i in range(n): 
            if i + 1 < n and word[i] == word[i+1]:
                continue
            if i + 1 < n and word[i+1] > word[i]:
                counts += 1
            else:
                if counts == 5:
                    max_length = max(max_length, i-l+1)
                    counts = 1
                    l = i + 1
                else:
                    counts = 1
                    l = i + 1
                

        return max_length



