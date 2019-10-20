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

int main(int argc, char *argv[]) {
  std::string line;
  std::getline(std::cin, line);
  std::istringstream iss(line);
  int N,M;
  iss >> N >> M;
  int* counts = new int[N+M]{0};

  int max = 0;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      counts[i+j]++;
      max = ((counts[i+j] > max) ? counts[i+j] : max);
    }
  }

  for (int i = 0; i < N+M; ++i) {
    if (counts[i]==max) std::cout << (i+2) << std::endl;
  }
}
