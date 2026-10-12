class Solution:
    def compress(self, chars: list[str]) -> int:
        processed = 0
        i = 0
        while i < len(chars):
            j = i
            while i + 1 < len(chars) and chars[i+1] == chars[i]:
                i+=1

            length = i - j + 1

            chars[processed] = chars[i]
            processed+=1
            if length > 1:
                length = str(length)
                for c in length:
                    chars[processed] = c
                    processed+=1

            i+=1
        
        return processed
