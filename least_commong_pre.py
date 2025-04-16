class Solution(object):
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_pre = ""
        word1 = strs[0]
        for idx in range(len(word1)):
            # helps pick out the character(letter) we are looking at
            for word_idx in range(1, len(strs)):
                if len(strs[word_idx]) <= idx:
                    return common_pre
                # helps pick out the word we are looking at
                if strs[word_idx][idx] != word1[idx]:
                    # makes sure charcters match, if they dont, return common prefix
                    return common_pre
            common_pre += word1[idx]
        return common_pre


def main():
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))


if __name__ == "__main__":
    main()
