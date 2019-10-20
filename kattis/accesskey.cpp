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
   std::string line("130");
   std::getline(std::cin, line);
   int N = std::stoi(line);
   std::unordered_map<std::string,bool> access_map;
   for (int i = 0; i < N; ++i) {
   std::getline(std::cin, line);
   std::string op, name;
   std::istringstream iss(line);
   bool anomaly(false);
   iss >> op >> name;
   auto entry = access_map.find(name); 
   if (op == "entry") {
      if (entry != access_map.end()) {
         bool entered = entry->second;
         if (entered) anomaly = true;
      }
      access_map[name] = true;
   } else if (op == "exit") {
      if (entry==access_map.end()) {
         anomaly = true;
      }
      else {
         if (entry->second==false) {
            anomaly = true;
         }
         access_map[name] = false;
      }
   }
   std::cout << name << " " << (access_map[name]==true ? "entered" : "exited") << " " << (anomaly?"(ANOMALY)":"") << "\n";
   } 
}
