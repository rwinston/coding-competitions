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

int main(int argc, char *argv[])
{
    std::string line;
  
   while(std::getline(std::cin, line)) {
       std::istringstream iss(line);
        int n,d;
        iss >> n >> d;
        if (n==0 && d==0) break;
        //unsigned long j = std::stoul(line);
        //std::cout << (j==0?1:(unsigned long)log10((long double)j)+1) << "\n";
        std::cout << ((int)n/d) << " " << ((int)n % d) << " / " << d << "\n";
    }
}
