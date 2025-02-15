from typing import List
def max_operations(nums:List[int],k:int)-> int:
    from collections import Counter
    counter = Counter(nums)
    count = 0
    
    for num in list(counter):
        complement = k-num
        if complement == num:
            count+=counter[num]//2
        elif complement in counter:
            pairs = min(counter[num], counter[complement])
            count+=pairs
            del counter[num], counter[complement]
    return count


def main():
    print(max_operations(nums = [1, 2, 3, 4], k = 5))  # Output: 2
    print(max_operations(nums = [3, 1, 3, 4, 3], k = 6))
if __name__ == "__main__":
    main()