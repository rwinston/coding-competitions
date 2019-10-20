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
   double n = std::stod(line);
   std::cout << pow(n, 1/n) << '\n';  
}
