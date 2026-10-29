class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in nums:
            if not map.get(i):
                map[i] = 1
            else:
                return True
        
        return False

        