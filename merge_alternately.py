def merge_alternatively(word1: str, word2: str)->str:
    length1 = len(word1)
    length2 = len(word2)
    result:str = ''
    ptr1 = 0
    ptr2 = 0

    while ptr1 < length1  and ptr2 < length2:
        result += word1[ptr1]
        result += word2[ptr2]
        ptr1+=1
        ptr2+=1

    while ptr1 < length1:
        '''
        word2 has ended
        '''
        result += word1[ptr1]
        ptr1+=1

    while ptr2 < length2:
        '''
        word1 has ended
        '''
        result += word2[ptr2]
        ptr2 += 1
    return result
def main():
    print(merge_alternatively(word1 = "abc", word2 = "pqr"))


main()
