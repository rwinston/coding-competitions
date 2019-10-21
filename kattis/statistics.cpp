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
   int idx=1;
   while (std::getline(std::cin, line)) {
      std::vector<int> data; 
      int n;
      std::istringstream iss(line);
      iss >> n;
      for (int i = 0; i < n; ++i) {
         int x;
         iss >> x;
         data.push_back(x); 
      }

   int min = *std::min_element(data.begin(), data.end());
   int max = *std::max_element(data.begin(), data.end());

   std::cout << "Case " << idx << ": " <<  min << " " << max << " " << (max-min) << "\n";
   idx++;
   }
}
