# https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_max_element(arr, low, high):
            if low == high:
                return low  # When there's only one element left, it's the maximum

            mid = (low + high) // 2  # Calculate the middle index
            if arr.get(mid) > arr.get(mid + 1):
                return find_max_element(arr, low, mid)  # The peak is in the left half
            else:
                return find_max_element(arr, mid + 1, high) 

        def binary(arr, l, t, r):
            while l <= r:
                mid = (l + r) // 2
                mid_value = arr.get(mid)
                if mid_value == t:
                    return mid
                elif mid_value > t:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        def binary2(arr, l, t, r):
            while l <= r:
                mid = (l + r) // 2
                mid_value = arr.get(mid)
                if mid_value == t:
                    return mid
                elif mid_value > t:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        l = 0
        r = mountain_arr.length() - 1
        ctr = find_max_element(mountain_arr, l, r)
        t = target 
        print(ctr)
        r = ctr 
        first = binary(mountain_arr, l, t, r)
        print(first)
        if first != -1:
            return first
        r= mountain_arr.length() - 1
        l = ctr+1 

        second = binary2(mountain_arr, l, t, r)
        print(second)
        return second
        
        return second