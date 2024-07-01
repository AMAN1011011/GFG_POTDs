class Solution { 
  public: 
    TreeNode* build_tree(int i, vector<int>&v, int n){ 
        if(i>=n)return NULL; 
        TreeNode* root=new TreeNode(v[i]); 
        root->left=build_tree(2*i+1,v,n); 
        root->right=build_tree(2*i+2,v,n); 
        return root; 
    } 
    void convert(Node *head, TreeNode *&root) { 
        vector<int>v; 
        Node* ptr=head; 
         
        while(ptr!=NULL){ 
            v.push_back(ptr->data); 
            ptr=ptr->next; 
        } 
        int n=v.size(); 
        root=build_tree(0,v,n); 
    } 
};
