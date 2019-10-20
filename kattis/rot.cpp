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

const std::string ROT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";

int main(int argc, char* argv[]) {
    std::string line;
    std::map<char,int> m;
    int i = 0;

    for (auto const& c : ROT) {
        m[c]=i++;
    }
    
    while (std::getline(std::cin,line)) {
        std::istringstream iss(line);
        int shift;
        std::string cipher, output;
        iss >> shift;
        if (shift==0) break;
        iss >> cipher;
        std::reverse(cipher.begin(), cipher.end());

        std::for_each(cipher.begin(), cipher.end(), [&output,&m,shift](char c) {    
            output += ROT[(int)((m[c]+shift)%(ROT.size()))];
        });

        std::cout << output << std::endl;
    }
}