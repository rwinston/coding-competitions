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


template<typename T>
void dump(const std::vector<T>& v) {
    std::for_each(v.begin(),v.end(),[](T v){std::cout << v << " ";});
    std::cout << '\n';
}


std::vector<int> rank(std::vector<int>& v) {
    std::vector<int> rank;
    int r=0;
    for (int i=0;i<v.size();++i) {
        r=1;
        for (int j=0;j<v.size();++j) {
            if (j!=i && (v[j]<v[i])) {
                r++;
            }
        }
       rank.push_back(r-1);
    }
    return rank;
}


int main(int argc, char* argv[]) {
  for (std::string line; std::getline(std::cin, line);) {
        int n = std::stoi(line);
        std::vector<int> l1,l2;

        for (int i = 0; i < n; ++i) {
            std::getline(std::cin, line);
            l1.push_back(std::stoi(line));
        }
        
        for (int i = 0; i < n; ++i) {
            std::getline(std::cin, line);
            l2.push_back(std::stoi(line));
        }

        std::vector<int> r = rank(l1);
        std::sort(l2.begin(), l2.end());
        
        for (int i = 0; i < n; ++i ) {
            std::cout << l2[r[i]] << '\n';
        }
        
        std::cout << std::endl;
  }
}