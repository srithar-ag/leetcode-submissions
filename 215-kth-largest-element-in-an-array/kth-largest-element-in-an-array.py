class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            i, j = left - 1, right + 1
            pivot = nums[(left + right) >> 1]
            while i < j:
                while True:
                    i += 1
                    if nums[i] >= pivot:
                        break
                while True:
                    j -= 1
                    if nums[j] <= pivot:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if j < target_index:
                return quickselect(j + 1, right)
            else:
                return quickselect(left, j)
        n = len(nums)
        target_index = n - k
        return quickselect(0, n - 1)
