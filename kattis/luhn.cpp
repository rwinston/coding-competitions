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
#include <tuple>
#include <utility>

int main(int argc, char *argv[])
{
  std::string line;
  std::getline(std::cin, line);
  int N = std::stoi(line);
 
  while (N>0) {
    std::getline(std::cin, line);
    int sum = 0;
  
    for (int j = line.size()-1; j>=0; --j) {
      int digit = line.at(j) - 48;
      int s = ((line.size()-j) % 2==0) ? digit*2 : digit;
      if (s>9) {
        s = (s%10) + ((s/10)%10);
      } 
      sum += s;
    }
    
    std::cout << ((sum%10)==0 ? "PASS" : "FAIL") << std::endl;
    N--;
  }
}