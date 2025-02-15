from typing import List
def increasing_triplet(nums:List[int])->bool:
    length = len(nums)
    left_min = [None]*length
    right_max = [None]*length

    left_min[0] = nums[0]
    right_max[length-1] = nums[length-1]
    for i in range(1, length):
        left_min[i] = min(left_min[i-1], nums[i])

    for i in range(length-2,-1,-1):
        right_max[i] = max(right_max[i+1], nums[i])

    for i in range(length):
        if left_min[i]<nums[i]<right_max[i]:
            return True
    return False

    """
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num<=first:
            first = num
        elif num<=second:
            second = num
        else:
            return True
    return False
    """


def main():
    print(increasing_triplet(nums = [1,2,3,4,5]))
    print(increasing_triplet(nums = [5,4,3,2,1]))
    print(increasing_triplet(nums=[2,1,5,0,4,6]))
main()