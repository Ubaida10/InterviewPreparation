#include<iostream>
#include<string>
using namespace std;

int value(char c)
{
    switch(c)
    {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }
}
int romanToInt(string str)
{
    int res = 0;
    int i = 0;
    while (i<str.length())
    {
        int val1 = value(str[i]);
        int val2 = value(str[i+1]);
        if(val1<val2)
        {
            res += abs(val1-val2);
            i = i+2;
        }
        else
        {
            res += val1;
            i++;
        }
    }
    return res;
}
int main()
{
    string s1 = "III";
    cout<<"The corresponding integer is: "<<romanToInt(s1)<<endl;

    string s2 = "LVIII";
    cout<<"The corresponding integer is: "<<romanToInt(s2)<<endl;

    string s3 = "MCMXCIV";
    cout<<"The corresponding integer is: "<<romanToInt(s3)<<endl;

    return 0;
}