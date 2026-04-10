class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i 
            len_str = ""
            word = ""
            while s[j] != "#":
                len_str += s[j]
                j += 1
            for idx in range(int(len_str)):
                word += s[j + 1 + idx]
            decoded_str.append(word)
            i += int(len_str) + 1 + len(len_str)
        return decoded_str