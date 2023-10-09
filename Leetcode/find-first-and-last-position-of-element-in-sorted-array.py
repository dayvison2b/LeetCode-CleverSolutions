# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(arr, target, low, high):
            if low > high:
                return [-1,-1]  # Target not found

            mid = (low + high) // 2

            if arr[mid] == target:
                result = [mid, mid]
                left = mid - 1
                right = mid + 1

                while left > -1 and arr[left] == target:
                    result[0] = left
                    left -= 1              

                while right < len(arr) and arr[right] == target:
                    result[1] = right
                    right += 1

                return result

            elif target < arr[mid]:
                return binarySearch(arr, target, low, mid - 1)  # Search in the left half
            else:
                return binarySearch(arr, target, mid + 1, high)  # Search in the right half
        return binarySearch(nums, target, 0, len(nums)-1)
        