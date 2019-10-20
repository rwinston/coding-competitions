#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <iomanip>

int main(int argc, char* argv[]) {
    std::string line;
    std::getline(std::cin,line);
    int n = std::stoi(line);    
    std::cout << std::fixed << std::setprecision(0) << (int)(pow(2,n)+1)*(pow(2,n)+1) << std::endl;
}