#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

int sumdigits(int n) {
    int s = 0;
    while (n > 0)
    {
        s += (n % 10);
        n /= 10;
    }
    return s;
}

int main(int argc, char *argv[])
{
   std::string line;
   std::getline(std::cin, line); 
   int N = std::stoi(line);
   
   for (int n=N;;n++) {
       int sum = sumdigits(n);
       if ((n % sum)==0) {
           std::cout << n << "\n";
           break;
       } 
   }
}