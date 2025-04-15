class Solution(object):
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = ["flower", "flow", "flight"]
        for i in strs:
            if i[0] == i[1]:
                print(i[0] + i[1])
            else:
                print("Error")
