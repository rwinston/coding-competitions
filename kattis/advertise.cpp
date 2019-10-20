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
    std::vector<int> usage;

    while (std::getline(std::cin,line)) {    
        std::istringstream iss(line);
        std::vector<int> data;
        data.insert(data.begin(), std::istream_iterator<int>(iss), std::istream_iterator<int>());
        int cost = (data[1]-data[2])-data[0];

        std::string s = (cost == 0) ? "does not matter" : ((cost>0) ? "advertise" : "do not advertise");
        std::cout << s << std::endl;
    }
    
}