import math
def gcd_of_strings(str1:str, str2:str):
    if str1+str2 != str2+str1:
        return ""
    max_length = math.gcd(len(str1), len(str2))
    return str1[0:max_length]



def main():
    print(gcd_of_strings(str1 = "ABCABC", str2 = "ABC"))

main()
