from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        re=[]
        for idx,str1 in enumerate(strs):
            result = []
            result.append(str1)
            for idx2,str2 in enumerate(strs[idx+1:]):
                count=0
                for x in str1:
                    if str2.find(x):
                        count=count+1
                if count==len(str1):
                    result.append(str2)

            re.append(result)

        return  re