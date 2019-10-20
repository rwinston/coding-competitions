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

struct point {
   int x;int y;
   point(int x, int y) { this->x=x; this->y=y;}
   inline const point operator+(const point& other) {
      return {other.x+x, other.y+y};
   }
};

std::ostream& operator<<(std::ostream& o, const point & p) {
   o << p.x << " " << p.y;
   return o;
}

int x(int digit) {
   switch (digit) {
      case 0: case 2: return 0; break;
      case 1: case 3: return 1; break;
   }
};

int y(int digit) {
   switch (digit) {
      case 0: case 1: return 0; break;
      case 2: case 3: return 1; break;
   }
};


point get_coord(std::string line, int zoom, point& p) {
   if (zoom==0) 
      return p;
   else {
    //std::cout << "get_coord(" << line << "," << zoom << "," << p << "\n";
    int delta = pow(2,zoom)/2;
     int digit = (int)line[0]-'0';
     p.x += x(digit)*delta;
     p.y += y(digit)*delta;
     return get_coord(line.erase(0,1), zoom-1, p);
   }
}

int main(int argc, char *argv[]) {
   std::string line("130");
   std::getline(std::cin, line);
   int zoom = size(line);
   point p(0,0);   
   int n = pow(2,zoom); // grid size
   //point coord = get_coord(line, zoom, p);
   std::cout << zoom << " " << get_coord(line, zoom, p);
}
