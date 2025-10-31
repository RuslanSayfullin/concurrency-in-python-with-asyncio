from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # Сокращаем префикс до тех пор, пока он не станет префиксом текущей строки
            while not current_string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix