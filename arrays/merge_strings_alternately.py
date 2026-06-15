# Problem: Merge Strings Alternately
# Platform: LeetCode
# Pattern: Array

# -------------------------------
# My Initial Approach (Verbose)
# -------------------------------




class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=''
        merge_list = []
        word1_list = list(word1)
        word2_list = list(word2)

        if len(word1) == len(word2):
            for i in range (len(word1)):
                merge_list.append(word1_list[i])
                merge_list.append(word2_list[i])
            merge = ''.join(merge_list)
        elif len(word1) >= len(word2):
            for i in range (len(word2)):
                merge_list.append(word1_list[i])
                merge_list.append(word2_list[i])
            
            merge = ''.join(merge_list)
            merge = merge + word1[len(word2):]

        elif len(word1) <= len(word2):
            for i in range (len(word1)):
                merge_list.append(word1_list[i])
                merge_list.append(word2_list[i])
            
            merge = ''.join(merge_list)
            merge = merge + word2[len(word1):]

        return merge
    
            

            


            
        
