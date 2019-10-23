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
#include <numeric>
#include <set>

template <typename T>
void dump(const std::vector<T> &v)
{
   std::for_each(v.begin(), v.end(), [](T v) { std::cout << v << ' '; });
   std::cout << '\n';
}
   int main(int argc, char *argv[]) {
   std::string line;
   std::getline(std::cin, line);
   int N = std::stoi(line);
   
   for (int i=0;i<N;++i) {
          std::getline(std::cin, line);
          //unsigned long j = std::stoul(line);
          //std::cout << (j==0?1:(unsigned long)log10((long double)j)+1) << "\n";
          std::cout << line.size() << "\n";
   }
}
