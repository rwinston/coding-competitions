#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>
#include <algorithm>

int min(int a, int b) { return (a<b)?a:b;}

int main(int argc, char *argv[])
{
   std::string line;
   std::getline(std::cin, line); 
   int N = std::stoi(line); //# cases
   
   for (int n=1;n<=N;++n) {
       std::getline(std::cin, line);
       int segments = std::stoi(line);
       std::getline(std::cin, line);
       std::istringstream iss(line);
       std::vector<int> red, blue;
       for (int i = 0; i < segments; ++i) {
           std::string segment;
           iss >> segment;
           if (segment.back()=='R') {
               segment.pop_back();
               red.push_back(std::stoi(segment));
           } else {
               segment.pop_back();
               blue.push_back(std::stoi(segment));
           }
       }

       std::sort(red.rbegin(), red.rend());
       std::sort(blue.rbegin(), blue.rend());

       int len=0;
       int N=min((red.size()),(blue.size()));
       for (int j = 0;j<N;j++) {
            len+=red[j];
            len+=blue[j];
            len-=2;           
       }     
       
       std::cout << "Case #" << n << ": " << len << "\n";

   } 
}