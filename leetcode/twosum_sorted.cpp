class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> solution;
        for (int i=0;i<numbers.size();++i) {
            int n = numbers[i];
            int complement = target-n;
            int j=bsearch(numbers, i+1, numbers.size()-1, complement);
            if (j!=-1) {
                solution.push_back(i+1);
                solution.push_back(j+1);
            }
        }
        return solution;
    }
    
    int bsearch(vector<int>& x, int start, int end, const int key) {
        if (start>end) return -1;
        int mid = start + ((end-start))/2;
        if (x[mid]==key) {
            return mid;
        }
        else if (x[mid]>key) {
            return bsearch(x, start, mid-1, key);
        }
        return bsearch(x, mid+1, end, key);
    }
  
};

