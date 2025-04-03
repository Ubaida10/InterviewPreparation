#include<bits/stdc++.h>
using namespace std;

int minSubArrayLength(int target, vector<int>& nums)
{
    int n = nums.size();
    int left = 0, right = 0, sum = 0, minLen = INT_MAX;
    while (right < n)
    {
        sum+=nums[right];
        while (sum>=target)
        {
            minLen = min(minLen, right-left+1);
            sum-=nums[left];
            left++;
        }
        right++;
    }
    return minLen == INT_MAX? 0 : minLen;
}
int main()
{
    vector<int> nums1 = {2,3,1,2,4,3};
    int target1 = 7;
    cout<<minSubArrayLength(target1, nums1)<<endl;

    vector<int> nums2 = {1,2,3,4,5};
    int target2 = 11;
    cout<<minSubArrayLength(target2, nums2)<<endl;
    return 0;
}