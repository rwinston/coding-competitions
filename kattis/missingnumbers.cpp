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

    int last=0; bool success(true);
    while (std::getline(std::cin,line)) {    
        int i = std::stoi(line);
        if ((i-last)>1) {
            success=false;
            while (++last!=i)std::cout << last << '\n';
        } else {
            last=i;
        }
    }
    if(success) std::cout << "good job\n";
    
}