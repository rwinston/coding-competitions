#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

int main(int argc, char* argv[]) {
    std::string line;
    std::getline(std::cin,line);
    
    while (std::getline(std::cin, line)) {
        long fact = std::stol(line);
        long x=1;
        while (fact>0) {x*=fact;fact--;}
        std::cout << x%10 << std::endl;

    }
}