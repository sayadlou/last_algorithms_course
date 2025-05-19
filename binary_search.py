from typing import List

abs(5)
def binary_search(nums: List[int], target: int) -> int:
    idx_left = 0
    idx_right = len(nums) - 1
    while idx_left <= idx_right:
        mid = (idx_right + idx_left ) // 2
        if target >  nums[mid]:
            idx_left = mid + 1
        elif target < nums[mid]:
            idx_right = mid - 1
        else :
            return mid
    return -1


if __name__ == "__main__":
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=3)
    assert  res== 2, res
    res = binary_search(nums=[1, 2, 3, 14, 15, 16, 17, 18, 19], target=18)
    assert res == 7, res
    print(1)
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=8)
    assert res == 7, res
    print(2)
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=9)
    assert res == 8, res
    print(3)
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=1)
    assert res == 0, res
    print(4)
    res = binary_search(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=2)
    assert res == 1, res
    print(5)
    res = binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9)
    assert res == 4, res
    print(6)
