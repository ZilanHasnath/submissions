from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                c1, c2 = w1[j], w2[j]
                if order_map[c1] < order_map[c2]:
                    break
                elif order_map[c1] > order_map[c2]:
                    return False
                    
        return True