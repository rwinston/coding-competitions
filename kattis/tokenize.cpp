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
    while (std::getline(std::cin,line)) {
      std::istringstream iss(line);
      std::string tmp,output;
      while (std::getline(iss,tmp,'-')) {
        output+=tmp[0];
      }
      std::cout << output << std::endl;   
    }

}