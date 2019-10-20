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
#include <bitset>
#include <cmath>

const int TIMEOUT(3*60+30);

int main(int argc, char* argv[]) {
   std::string line;
   std::getline(std::cin,line);
   int p = std::stoi(line);
   std::getline(std::cin,line);
   int q = std::stoi(line);
   int t =0; 


   for (int i = 0; i < q; ++i) {
      std::getline(std::cin,line);
      std::istringstream iss(line);
      int qt; std::string ans;
      iss >> qt >> ans;
      t+=qt;
      if (t>=TIMEOUT) break;
      if (ans=="T") {
         p = (p==8) ? 1 : (p+1); 
      }
   }

   std::cout << p << std::endl;
}