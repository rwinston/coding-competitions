#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

int main(int argc, char* argv[]) {
    std::string line;
    //std::ifstream fin(argv[1]);

    int x,y;
    std::getline(std::cin,line);
    std::istringstream is( line );
    std::vector<int> dimensions = std::vector<int>(std::istream_iterator<int>(is), std::istream_iterator<int>());
    
    while (std::getline(std::cin , line)) {
        int m = std::stoi(line);
       if ((m<=dimensions[1]) || (m<=dimensions[2]) || (m<=sqrt(dimensions[1]*dimensions[1]+dimensions[2]*dimensions[2]))) {
            std::cout << "DA" << std::endl;
        }
        else {
            std::cout << "NE" << std::endl;
        }
    }
}