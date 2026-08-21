class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_table = {}
        ans = list()

        # iterate through numbers
        for i, val in enumerate(nums):
            if val in h_table: 
                # if table already contain the value
                key = h_table.get(val)
                ans.append(key)
                ans.append(i)
                
                break

            else:
                # needed value to get the target
                needed_val = target - val
                # update the hash table
                h_table[needed_val] = i

        return ans