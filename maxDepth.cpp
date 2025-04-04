#include<iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode() : val(0), left(nullptr), right(nullptr){}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


int intmaxDepth(TreeNode *node){
    if(node==nullptr){
        return 0;
    }
    else{
        int leftDepth = intmaxDepth(node->left);
        int rightDepth = intmaxDepth(node->right);
        return max(leftDepth, rightDepth) + 1;
    }
} 


int main() {
    return 0;
}