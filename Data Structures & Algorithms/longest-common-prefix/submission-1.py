class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the array based on the string length
        strs.sort(key=lambda str: len(str))

        # use the first array as the one to compare

        longest_prefix = strs[0]

        for str in strs:
            # compare each character
            if str == strs[0]:
                continue # skip the first iteration

            for i in range(0, len(longest_prefix)):
                if str[i] != longest_prefix[i]:
                    # if the character not matched
                    longest_prefix = longest_prefix[:i]
                    # cut the rest
                    break
            

        return longest_prefix
