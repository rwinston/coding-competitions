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


bool can(int a, int b, int c){
  if ((a+b) == c) return true;
  if ((a-b) == c) return true;  
  if ((b-a) == c) return true;
  if ((a*b) == c) return true;
  int d = a/b;
  if (d==c && d*b==a) return true;
  d = b/a;
  if (d==c && d*a==b) return true;
  return false;

}
int main(int argc, char* argv[]) {
   std::string line;
   std::getline(std::cin, line);
   int N = std::stoi(line);

   while ((N--)>0) {
    std::getline(std::cin,line);
    int a,b,c;
    std::istringstream iss(line);
    iss >> a >> b >> c;
    std::cout << ((can(a,b,c)) ? "Possible" : "Impossible") << std::endl;
  }  
}