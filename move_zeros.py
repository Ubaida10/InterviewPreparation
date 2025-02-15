from typing import List
def move_zeros(nums: List[int]) -> None:
    """"
    length = len(nums)
    for i in range(length):
        if nums[i] == 0:
            for j in range(i+1, length):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
    print(nums)
    return
    """

    length = len(nums)
    i = 0
    for j in range(length):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    print(nums)

def main():
    print(move_zeros(nums = [0, 1, 0, 3, 12]))
    print(move_zeros(nums = [0]))
    print(move_zeros(nums = [2, 1]))
    print(move_zeros(nums = [0, 1, 0, 3, 0]))
    print(move_zeros(nums = [1, 0, 1]))


main()
