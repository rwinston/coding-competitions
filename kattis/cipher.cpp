#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

int main(int argc, char* argv[]) {
    std::string cipher;
    std::getline(std::cin, cipher);
    std::string comp;
    int len = (int)cipher.size()/3;
    for (int i = 0; i < len; ++i) { comp.append("PER");}
    int distance = 0;
    for (int j = 0; j < cipher.size(); ++j) {
        if (cipher[j]!=comp[j]) distance++;
    }
    std::cout << distance << std::endl;
}