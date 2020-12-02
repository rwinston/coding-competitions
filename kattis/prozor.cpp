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

int max(int a, int b) { return (a>b)?a:b;}


template <typename T>
void dump(const std::vector<T> &v)
{
   std::for_each(v.begin(), v.end(), [](T v) { std::cout << v << ' '; });
   std::cout << '\n';
}

void dump_grid_and_racket(char** grid, int r, int c,int mr,int mc, int k) {
   for (int i=mr;i<mr+k;++i) {
      for (int j=mc;j<mc+k;++j) {
        // std::cout << "i=" << i << ",j=" << j << "grid[i][j]=" << grid[i][j] << '\n';
         if (i==mr || i == (mr+k-1)) {
            if (j==mc || j==mc+k-1) { grid[i][j]='+';}
            else { grid[i][j]='-';}
         }
         else if (j==mc || j==mc+k-1) { grid[i][j]='|';}
      }
   }

   for (int i=0;i<r;++i) {
      for (int j=0;j<c;++j) {
         std::cout << grid[i][j];
      }
      std::cout << '\n';
   }
}

int count_whacks(char** grid, int i, int j, int k) {
   int whacks=0;
   for (int ii=i+1;ii<i+k-1;++ii) {
      for (int jj=j+1;jj<j+k-1;++jj) {
         if (grid[ii][jj]=='*')
            whacks++;
      }
   }
   return whacks;
}

int main(int argc, char *argv[]) {
   std::string line;
   int r,s,k=0;
   std::getline(std::cin,line);
   std::istringstream iss(line);
   iss >> r >> s >> k;
   
   char** grid = new char*[r];
   for (int i=0;i<r;++i) {
      grid[i] = new char[s];
   }

   for (int i = 0; i < r; ++ i) {
      std::getline(std::cin, line);
      for (int j=0;j<s;j++) {
         grid[i][j] = line[j];
      }
   }

   // iterate over the grid
   // x moves from 0 to c-k
   // y moves from 0 to r-k
   int whacks=0,mr=0,mc=0;
   for (int i=0;i<r-k+1;++i){
      for (int j=0; j<s-k+1;++j) {
         int w = count_whacks(grid, i, j, k);
         if (w>whacks){
            whacks=w;
            mr=i;mc=j;
         }
      }
   }

   std::cout << whacks << std::endl;   
   dump_grid_and_racket(grid, r, s, mr, mc,k);
}
