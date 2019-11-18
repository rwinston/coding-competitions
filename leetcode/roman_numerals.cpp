class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int> codes;
        codes['I'] = 1; 
        codes['V'] = 5; 
        codes['X'] = 10; 
        codes['L'] = 50; 
        codes['C'] = 100; 
        codes['D'] = 500; 
        codes['M'] = 1000; 
        
        int sum = 0;
        for (int i =0; i < s.size(); ++i) {
            char c = s[i];
            sum += codes[c];
            if (i>0) {
                if (codes[s[i-1]]<codes[s[i]])
                    sum -= 2*codes[s[i-1]];
            }
        }

        return sum;
    }
};
