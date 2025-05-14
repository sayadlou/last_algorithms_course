from typing import List


def binary_search(nums: List[int], target: int) -> int:
    idx_left = 0
    l: int = len(nums)
    idx_right = l // 2
    while True:
        if target > nums[idx_right]:
            idx_left += idx_right
            idx_right *= 2
        elif target < nums[idx_right]:
            idx_right  =  idx_right //2
            
        elif nums[idx_right] == target:
            print(idx_right)
            return idx_right


if __name__ == "__main__":
    # res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=3)
    # assert  res== 2, res
    res = binary_search(nums=[1, 2, 3, 14, 15, 16, 17, 18, 19], target=18)
    assert res == 7,res
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=8)
    assert res == 7, res
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=9)
    assert res == 8, res
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=1)
    assert res == 0, res
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=2)
    assert res == 1, res
