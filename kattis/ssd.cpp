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

std::vector<int> digits(int x,int b) {
  unsigned int s=x;
  std::vector<int> r;
  while (s>0) {
    r.push_back(s%b);
    s/=b;
  }
  std::reverse(r.begin(),r.end());
  return r;
}

int main(int argc, char* argv[]) {
    std::string line;
    std::getline(std::cin,line);  

    while (std::getline(std::cin,line)) {
      std::istringstream iss(line);
      int i, base, n;
      iss >> i >> base >> n;
      int sum=0, j=0;
    
      for (int digit : digits(n,base)) {
        sum+=digit*digit;
      }

      std::cout << i << " " << sum << std::endl;
    }

}