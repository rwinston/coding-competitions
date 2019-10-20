#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <map>

int main(int argc, char* argv[]) {
    std::string line;
    std::vector<std::string> hand;
    std::getline(std::cin,line);
    std::map<char,int> m;
    std::istringstream iss(line);

    std::copy(std::istream_iterator<std::string>(iss), 
        std::istream_iterator<std::string>(),std::back_inserter(hand));

    for (std::string i : hand) {
        m[i[0]]++;
    } 

    auto rank = std::max_element(m.begin(), m.end(), [](const std::pair<char,int> a, const std::pair<char,int> b){
        return a.second < b.second;
    });
    
    std::cout << rank->second << std::endl;
}