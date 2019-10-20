#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

int sumdigits(int x) {
    if (x<10) return x;
    else {
        int b=x;
        int sum=0;
        while (b>0) {
           sum+=b%10;
           b/=10;
        }
        return sum;
     }
}

int main(int argc, char* argv[]) {
    std::string line;
    int L,D,X;

    std::getline(std::cin, line);
    L = std::stoi(line);

    std::getline(std::cin, line);
    D = std::stoi(line);
    
    std::getline(std::cin, line);
    X = std::stoi(line);
    
    int min=10000,max=0;

    for (int j=L;j<=D;++j) {
        int s = sumdigits(j);
        if ((s==X) && (j>max)) max=j;
        if ((s==X) && (j<min)) min=j;
    }

    std::cout << min << std::endl << max << std::endl;
}