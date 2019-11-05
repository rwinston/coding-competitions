// you can use includes, for example:
// #include <algorithm>
#include<vector>
#include<algorithm>
#include<stack>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int N) {
    // write your code in C++14 (g++ 6.2.0)
    int n=N;
    int maxgap=0;
    bool ingap=false;
    int gap=0;
    while (n!=0) {
        int bit = (n%2);
        if (bit==1) {
               if (ingap && gap>0) {
                maxgap = (maxgap<gap)?gap:maxgap;
                gap=0;
               }
               else {
                  ingap=true; 
               }
        }
        else {
          gap++;
        }
        n /=2;
    }
    
    return maxgap;
    
    
}

