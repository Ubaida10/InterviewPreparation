from typing import List
def can_place_flower(flowerbed:List[int], n:int)->bool:
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i-1] == 0)
            empty_right = (i == length-1) or (flowerbed[i+1] == 0)
            if empty_left and empty_right:
                flowerbed[i] = 1
                count+=1
    return count>=n


def main():
    print(can_place_flower(flowerbed = [1,0,0,0,1], n = 1))
    print(can_place_flower(flowerbed=[1, 0, 0, 0, 1], n=2))


main()