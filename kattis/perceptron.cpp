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
    std::vector<std::vector<int>> x;
    std::vector<int> y;

    while (std::getline(std::cin,line)) {    
        std::istringstream iss(line);
        std::vector<int> xi;
        xi.insert(xi.begin(), std::istream_iterator<int>(iss), std::istream_iterator<int>());
        y.push_back(xi.back());
        xi.pop_back();
        x.push_back(xi);
    }

    std::for_each(x.begin(), x.end(), [](std::vector<int> x_i){
        for (auto i: x_i) {
            //std::cout << i << " ";
        }
        //std::cout << std::endl;
        });

        std::cout << "Read " << x.size() << " lines" << std::endl;
    
}