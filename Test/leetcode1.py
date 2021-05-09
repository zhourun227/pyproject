from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        num=0
        for i in range (len(guess)):
            if guess[i]==answer[i]:
                num+=1
            else:
                pass
        print(num)
        return num
s=Solution()
s.game([1,2,3],[1,2,2])

