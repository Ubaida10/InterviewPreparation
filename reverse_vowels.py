def reverse_vowels(word:str)->str:
    left = 0
    word = list(word)
    right = len(word)-1
    vowels = 'aeiouAEIOU'
    while left<right:
        if word[left] in vowels and word[right] in vowels:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        elif word[left] in vowels:
            right-=1
        else:
            left += 1
    return "".join(word)
def main():
    print(reverse_vowels(word="IceCreAm"))
main()