#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

int main(int argc, char* argv[]) {
    std::string line;
    std::getline(std::cin, line);
    const char* p = line.c_str();
    const char* q = p+1;
    std::cout << *p;   
    for (;*q;p++,q++) {
        if (*p != *q) {
            std::cout << *q ;
        }
    }
    std::cout << std::endl;
}