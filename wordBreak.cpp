#include<bits/stdc++.h>
using namespace std;

bool wordBreak(string s, vector<string>& wordDict){
    int n = s.size();
    
    vector<bool> dp(n+1, false);
    int i,j;
    
    dp[0] = true;
    for(i = 1; i <= n; i++){
        for (j = 0; j < i; j++){
            if(dp[j] && find(wordDict.begin(), wordDict.end(), s.substr(j, i-j)) != wordDict.end()){
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}


int main(){
    string s = "leetcode";
    vector<string> dict = {"leet","code"};
    if(wordBreak(s, dict)){
        cout<<"true"<<endl;
    }
    else{
        cout<<"false"<<endl;
    }
    return 0;
}