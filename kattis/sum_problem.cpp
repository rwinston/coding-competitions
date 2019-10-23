#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>



int main(int argc, char *argv[])
{
   std::string line;
   std::getline(std::cin, line); 
   int N = std::stoi(line);
   
   for (int i=0;i<N;i++) {
          std::getline(std::cin, line); 
          std::istringstream iss(line);
          int x,p;
          int sum=0,oddsum=0,evensum=0;
          iss >> x >> p;
          for (int j=1;j<=p;++j) {
             sum+=j;
          }
          for (int j=1,i=0;i<p;j+=2,i++){
              oddsum+=j;  
          }
          for (int j=2,i=0;i<p;j+=2,i++){
              evensum+=j;  
          }
          std::cout << x << " " << (sum) << " " << oddsum << " " << evensum << "\n";
   }
}