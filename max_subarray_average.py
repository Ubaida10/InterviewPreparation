from typing import List
def find_max_average(nums, k):
    left = 0
    max_average = float('-inf')
    right = 0 + (k - 1)
    curr_sum = sum(nums[left:right + 1])
    
    while right < len(nums) - 1:
        max_average = max(curr_sum / k, max_average)
        curr_sum -= nums[left]
        left += 1
        right += 1
        curr_sum += nums[right]
    max_average = max(curr_sum / k, max_average)  
    return max_average
def main():
    print(find_max_average(nums = [1,12,-5,-6,50,3], k = 4))
    print(find_max_average(nums = [5], k = 1))

if __name__ == "__main__":
    main()