#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

int sumdigits(int n) {
    int s = 0;
    while (n>0) {
        s+=(n%10);
        n/=10;
    } 
    return s;
}

int main(int argc, char* argv[]) {
    std::string line("3029");
    while (std::getline(std::cin, line)) {
        
        int N = std::stoi(line);
        if (N==0) break;
        int sum = sumdigits(N);
        
        for (int p = 11;;p++) {
            int Np = sumdigits(N*p);
            if (Np==sum) {
                std::cout << p << std::endl;
                break;

            }
        }
   }
}