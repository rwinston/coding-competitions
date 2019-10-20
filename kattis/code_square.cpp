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

int main(int argc, char *argv[])
{
  std::string line;
  std::getline(std::cin, line);
  int N = std::stoi(line);

  while ((N--) > 0) {
    std::getline(std::cin, line);
    const int n = (int)sqrt(line.size());
    char **vec = new char *[n];
    for (int i = 0; i < n; ++i)
      vec[i] = new char[n];

    const char *p = line.c_str();
    for (int i = 0; i < n; ++i)
      for (int j = n - 1; j >= 0; j--)
        vec[j][i] = *p++;

    for (int i = 0; i < n; ++i){
      for (int j = 0; j < n; ++j){
        std::cout << vec[i][j];
      }
    }

    std::cout << std::endl;
  }
}
