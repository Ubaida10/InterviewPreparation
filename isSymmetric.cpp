#include<bits/stdc++.h>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *l, TreeNode *r) : val(x), left(l), right(r) {}
};

bool isMirror(TreeNode* root1, TreeNode* root2){
    if(root1 == nullptr && root2 == nullptr){
        return true;
    }
    if(root1 == nullptr || root2 == nullptr){
        return false;
    }
    return (root1->val == root2->val) && isMirror(root1->left, root2->right) && isMirror(root1->right, root2->left); 
}

bool isSymmetric(TreeNode* root) {
    if (!root) return true;
    return isMirror(root->left, root->right);
}

int main(){

    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);
    cout << isSymmetric(root) << endl; // true
    return 0;
}