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

const double PI(3.14159265358979323846);

int main(int argc, char* argv[]) {
   std::string line;
   std::getline(std::cin,line);
   std::istringstream iss(line);
   int h,d;
   iss >> h >> d;
   std::cout << (int)ceil((double)h/sin((PI/180.0)*d)) << std::endl;
}