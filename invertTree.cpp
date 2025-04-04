#include<bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


TreeNode* invertTree(TreeNode* root){
    if (root == NULL) return NULL;

    else{
        TreeNode* left = invertTree(root->left);
        TreeNode* right = invertTree(root->right);
        root->left = right;
        root->right = left;
    }
    return root;
}

void printTree(TreeNode* root){
    cout<<"Printing in DFS Order: ";
    if(root == nullptr) return;
    printTree(root->left);
    cout<<root->val<<" ";
    printTree(root->right);
    cout<<endl;

    cout<<"Printing in BFS Order: ";
    queue<TreeNode*> q;
    q.push(root);
    while(!q.empty()){
        TreeNode* curr = q.front();
        q.pop();
        cout<<curr->val<<" ";
        if(curr->left) q.push(curr->left);
        if(curr->right) q.push(curr->right);
    }
    cout<<endl;
}
int main(){
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(7);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(9);
    TreeNode* inverted = invertTree(root);
    
    // Your code to print the inverted tree here
    printTree(inverted);
    return 0;;
}