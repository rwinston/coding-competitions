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

std::vector<int> get_digits(std::string s) {
   std::vector<int> v;
   for (char& c: s) {
      v.push_back(c-'0');
   }
   return v;
}

int main(int argc, char *argv[]) {
   std::string line("330");
   std::getline(std::cin, line);
   int x = std::stoi(line);
   std::vector<int> digits = get_digits(line);
   std::vector<int> results;
   
   do {
         int result = 0;
         for (auto& a : digits) {
            result = result*10+a;
         }
         if (result>x) results.push_back(result);
   } while (std::next_permutation(digits.begin(), digits.end()));

   if (results.size()==0) results.push_back(0);
   std::cout << *std::min_element(results.begin(), results.end()) << "\n";

}
