class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        basket = defaultdict(int)

        l = 0
        r = 0
        picked = 0
        while l < len(fruits):
            if r >= len(fruits):
                break
            if (fruits[r] in basket or len(basket) < 2):
                basket[fruits[r]] += 1
                r+=1
            else:
                picked = max(picked, r - l)
                while l < r-1:
                    basket[fruits[l]] -= 1
                    if basket[fruits[l]] == 0:
                        del basket[fruits[l]]
                        l+=1
                        break
                    l+=1
         
        return max(picked, r - l)
