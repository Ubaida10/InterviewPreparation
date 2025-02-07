from typing import List
def kids_with_candies(candies: List[int], extra_candies) -> List[bool]:
    max_candies = max(candies)
    length = len(candies)
    result = [False]*length

    for i in range(length):
        if candies[i]+extra_candies>=max_candies:
            result[i] = True

    return result


def main():
    print(kids_with_candies(candies = [2,3,5,1,3], extra_candies = 3))
    print(kids_with_candies(candies = [4,2,1,1,2], extra_candies = 1))

main()