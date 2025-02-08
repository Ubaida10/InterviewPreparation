def reverse_words(s:str)->str:
    words = s.strip()

    text = words.split()

    length = len(text)

    for i in range(length//2):
        text[i], text[length-i-1] = text[length-i-1], text[i]

    return " ".join(text)
def main():
    print(reverse_words(s = "  hello world  "))

main()