class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = []
        for char in t:
            t_list.append(char)
        for char in s:
            if char not in t_list:
                return False
            t_list.remove(char)
        if len(t_list) == 0:
            return True
        return False


