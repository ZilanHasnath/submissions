from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        ref = strs[0]
    
        for word in strs[1:]:
            i = 0
            while i < len(ref) and i < len(word) and ref[i] == word[i]:
                i += 1
            ref = ref[:i]
            if not ref:
                break
                
        return ref