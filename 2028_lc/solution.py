class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        total = mean * (len(rolls) + n)
        curr_sum = sum(rolls)
        need = total - curr_sum
        if 6 * n < need or need < n:
            return []

        res = [1] * n
        need -= n
        counter = 0
        if need == 0:
            return res

        while need > 5:
            need -= 5
            res[counter] +=5
            counter += 1

        res[counter] += need

        return res

            
