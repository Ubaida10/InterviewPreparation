#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

int candy(vector<int>& ratings)
{
    int n = ratings.size();
    vector<int> candies(n, 1);
    
    //left pass
    for(int i = 1; i < n; i++)
    {
        if(ratings[i] > ratings[i-1])
        {
            candies[i] = candies[i-1]+1;
        }
    }

    //right pass
    for(int i = n-2; i >= 0; i--)
    {
        if(ratings[i]>ratings[i+1])
        {
            candies[i] = max(candies[i],candies[i+1]+1);
        }
    }
    return accumulate(candies.begin(), candies.end(), 0);
}

int main()
{
    vector<int> ratings1 = {1, 0, 2};
    cout << candy(ratings1) << endl;
    
    vector<int> ratings2 = {1, 2, 2};
    cout << candy(ratings2) << endl;
    
    vector<int> ratings3 = {1, 3, 2, 2, 1};
    cout << candy(ratings3) << endl;
    return 0;
}