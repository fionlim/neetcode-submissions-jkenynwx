class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = dict()
        for char in s:
            if char in temp:
                temp[char] += 1
            else:
                temp[char] = 1
        flag = True
        for char in t:
            if char in temp:
                temp[char] -= 1
                if temp[char] == 0:
                    flag = temp.pop(char, False)
            else:
                return False
        if len(temp.keys()) == 0 and flag is not False:
            return True
        return False

