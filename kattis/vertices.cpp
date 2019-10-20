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

int main(int argc, char* argv[]) {
    std::string line;
    std::unordered_map<int,int> mymap_x;
    std::unordered_map<int,int> mymap_y;

    while (std::getline(std::cin, line)) {
        std::istringstream is(line);
        std::vector<int> points = std::vector<int>(std::istream_iterator<int>(is), std::istream_iterator<int>());
        mymap_x[points[0]]++; mymap_y[points[1]]++;
    }

    int x,y;
    std::unordered_map<int,int>::iterator it = mymap_x.begin();
    std::for_each(mymap_x.begin(), mymap_x.end(), [&x](std::pair<int,int> element) {
        if (element.second==1) x=element.first;
    });

    it = mymap_y.begin();
    std::for_each(mymap_y.begin(), mymap_y.end(), [&y](std::pair<int,int> element) {
        if (element.second==1) y=element.first;
    });

    std::cout << x << " " << y << std::endl;
}