class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first = {"Q", "W", "E","R","T","Y","U","I","O","P"}
        second = {"A","S","D","F","G","H","J","K","L"}
        third = {"Z","X","C","V","B","N","M"}
        res = []
        for word in words:
            upper_word = word.upper()

            first_char = upper_word[0]
            set_to_check = None
            if first_char in first:
                set_to_check = first
            elif first_char in second:
                set_to_check = second
            else:
                set_to_check = third
            
            good = True
            for char in upper_word:
                if char not in set_to_check:
                    good = False
                    break
            
            if good:
                res.append(word)
            
        return res
            


