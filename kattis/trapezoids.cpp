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
    double sum = 0, N=std::stoi(line);
    bool first_pass = true;

    std::vector<std::vector<double>> readings;
    for (int i=0;i<N;++i) {
        std::getline(std::cin,line);
        std::istringstream is(line);
        std::vector<double> entry = std::vector<double>(std::istream_iterator<double>(is), std::istream_iterator<double>());
        std::cout << std::setprecision(7);
        if (first_pass) {
            first_pass=false;
        }
        else {
             std::vector<double> prev = readings.back();
             sum += (entry[1]+prev[1])/2*(entry[0]-prev[0]);    
        }
        readings.push_back(entry);
    }

    std::cout << sum/1000 << std::endl;
}