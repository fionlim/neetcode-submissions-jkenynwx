class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution using acsii values

        # acsii vals mapped to list of strings
        # vals = {} 
        # for i in strs:
        #     val = 0
        #     for char in i:
        #         val += ord(char)
        #     if val in vals:
        #         vals[val].append(i)
        #     else:
        #         vals[val] = [i,]
        # return list(vals.values())


        hashmap = dict()
        for i in strs:
            arr = [0,] * 26
            for char in i:
                arr[ord(char) - ord('a')] += 1
            arr = str(arr)
            if arr in hashmap:
                hashmap[arr].append(i)
            else:
                hashmap[arr] = [i,]
        return list(hashmap.values())

        
