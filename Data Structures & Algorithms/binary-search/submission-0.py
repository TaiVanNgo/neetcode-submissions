class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
                
        while(lower <= upper):
            mid = (lower + upper) // 2

            if target == nums[int(mid)]:
                return mid

            if target < nums[mid]:
                upper = mid - 1
            elif(target > nums[mid]): 
                lower = mid + 1

        return -1