#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>
#include <algorithm>
#include <iomanip>

void dump(const std::vector<double>& v) {
    std::for_each(v.begin(),v.end(),[](double v){std::cout << v << std::endl;});
}

int main(int argc, char* argv[]) {
    std::string line;
    std::getline(std::cin,line);
    int sum = 0, N=std::stoi(line);

    std::getline(std::cin,line);
    std::istringstream is(line);
    std::vector<int> entry = std::vector<int>(std::istream_iterator<int>(is), std::istream_iterator<int>());

    for_each(entry.begin(), entry.end(), [&sum](int x) {
        if (x<0) sum=sum+x;
    });


    std::cout << sum*-1 << std::endl;
}