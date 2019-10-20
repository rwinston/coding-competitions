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
    double sum = 0;
    
    while (std::getline(std::cin, line)) {
        std::istringstream is(line);
        std::vector<double> entry = std::vector<double>(std::istream_iterator<double>(is), std::istream_iterator<double>());
        sum+=entry[0]*entry[1];
    }
    std::cout << sum << std::endl;
}