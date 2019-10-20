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
    int bw = std::stoi(line);
    std::vector<int> usage;

    std::getline(std::cin,line);

    while (std::getline(std::cin,line)) {    
        usage.push_back(std::stoi(line));
    }
    
    int sum = 0;
    std::for_each(usage.begin(), usage.end(), [&sum,bw](int n){sum+=(bw-n);});
    std::cout << sum+bw << std::endl;
}