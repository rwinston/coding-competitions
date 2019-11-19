class Solution {
public:
    string intToRoman(int num) {
        unordered_map<int,char> codes;
        codes[1] = 'I'; 
        codes[5] = 'V'; 
        codes[10] = 'X'; 
        codes[50] = 'L'; 
        codes[100] = 'C'; 
        codes[500] = 'D'; 
        codes[1000] = 'M'; 
        

        int x = num; int tens=1;
        string s;
        while (x>0) {
            string out;
            int digit = x%10;
            if (digit>=1 && digit<=3) {
                char c = codes[tens];
                out.append(digit,c); 
            }
            else if (digit==4) {
                out.append(1,codes[tens]);
                out.append(1,(char)codes[5*tens]);
            }
            else if (digit==5) {
                out.append(1,codes[5*tens]);
            }
            else if (digit>=6 && digit<9) {
                out.append(1,codes[5*tens]);
                out.append(digit-5,codes[tens]);
            }
            else if (digit==9) {
                out.append(1,codes[tens]);
                out.append(1, codes[10*tens]);
            }
            x/=10;
            tens*=10;
            s.insert(0,out);
        }
        
        cout << s << endl;
        return s;
        
        
    }
};
