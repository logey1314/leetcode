from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        lst=[]
        for str1 in strs:
            str_sort=''.join(sorted(str1))
            if str_sort not in hash_map.keys():
                hash_map[str_sort]=[]
                hash_map[str_sort].append(str1)
            else:
                hash_map[str_sort].append(str1)

        for list_val in hash_map.values():
            lst.append(list_val)
        return  lst




