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

int main(int argc, char *argv[])
{
   std::string line;
   int n = 0;
   std::getline(std::cin, line);
   n = std::stoi(line);

   while (n != -1)
   {

      int **A = new int *[n];
      for (int i = 0; i < n; ++i)
         A[i] = new int[n];

      for (int i = 0; i < n; ++i)
      {
         std::getline(std::cin, line);
         std::istringstream iss(line);
         for (int j = 0; j < n; ++j)
         {
            iss >> A[i][j];
         }
      }

      std::vector<int> weak_vertices;

      for (int i = 0; i < n; ++i)
      { // each vertex
         std::vector<int> indices;
         bool weak = true;
         for (int j = 0; j < n; ++j)
         { // each element
            // find neighbours
            if (A[i][j] == 1) {
               indices.push_back(j);
            }
         }

         if (indices.size() > 0) {
            for (int a = 0; a < indices.size() - 1; ++a) {
               for (int b = a+1; b < indices.size(); ++b) {
                  //std::cout << indices[a] <<","<< indices[b]<<'\n';
                  if (A[indices[a]][indices[b]] == 1) {
                     weak = false; 
                     break;
                  }
               }
               if (!weak) break;
            }
            indices.clear();
            if (weak) {
               weak_vertices.push_back(i);
            }
         } else {
               weak_vertices.push_back(0);
         }
      }

      dump(weak_vertices);
      delete[] A;
      std::getline(std::cin, line);
      n = std::stoi(line);
   }
}
