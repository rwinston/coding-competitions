class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        set<int> s;
        populate(root, s);
        bool found=false;
        for (int i:s) {
            int t=k-i;
            auto it=s.find(t);
            found=(it!= s.end() && (*it!=i));
            if (found) break;
        }
        return found;
    }
    
    void populate(const TreeNode* root, set<int>& s) {
        if (root) s.insert(root->val);
        if (root->left) populate(root->left,s);
        if (root->right) populate(root->right,s);
    }
};

