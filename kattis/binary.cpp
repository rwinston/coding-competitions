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

int from_vec(std::vector<int> x, int b) {
  int result=0,j=0;
  for (int i=x.size()-1;i>=0;i--) {
    result+=x[i]*pow(b,j++);
  }
  return result;
}

int main(int argc, char* argv[]) {
   std::string line;
   while (std::getline(std::cin,line)) {
     int x = std::stoi(line);
     std::vector<int> binary = digits(x,2);
     std::reverse(binary.begin(), binary.end());
     std::vector<int> decimal = digits(from_vec(binary,2),10);
     std::cout << from_vec(decimal,10) << std::endl;
   }
  
}