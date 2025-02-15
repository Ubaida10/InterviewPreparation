from typing import List
def max_area(height:List[int])->int:
    left = 0
    right = len(height)-1
    max_area = 0

    while left<right:
        max_area = max(max_area, min(height[left], height[right])*(right-left))
        if height[left]<height[right]:
            left += 1
        else:
            right -= 1
    return max_area


def main():
    print(max_area([1,8,6,2,5,4,8,3,7]))  # Expected output: 49
    print(max_area([1,1]))  # Expected output: 1

if __name__ == "__main__":
    main()