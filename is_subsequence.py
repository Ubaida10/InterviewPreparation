def is_subsequence(s:str, t:str) -> bool:
    # Your implementation here
    s_length = len(s)
    t_length = len(t)
    i, j = 0, 0
    while i < s_length and j < t_length:
        if s[i] == t[j]:
            i+=1
        j+=1
    return i == s_length


def main():
    print(is_subsequence("abc", "ahbgdc"))  # True
    print(is_subsequence("axc", "ahbgdc"))  # False

main()