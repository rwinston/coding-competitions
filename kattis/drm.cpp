#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>
#include <algorithm>
#include <iomanip>


int calc_rot(const std::string& s) {
    int sum = 0;
    for (int j=0;j<s.size();++j) {
        sum+=(s[j]-65);
    }
    return sum;

}

char rotate(char c, int rot) {
    return (char)65+(((c-65)+rot)%26);
}

int main(int argc, char* argv[]) {
    std::string line;
    std::getline(std::cin, line);
    int sz = line.size();
    // divide
    int rot1 = calc_rot(line.substr(0, sz/2));
    int rot2 = calc_rot(line.substr(sz/2, line.npos));
    char* r1 = new char[sz/2];
    char* r2 = new char[sz/2];
    
    for (int j = 0; j < sz; ++j) {
        if (j<sz/2) {
            r1[j]=rotate(line[j], rot1);
        } else {
            r2[j-(sz/2)]=rotate(line[j], rot2);
        }
    }

    for (int j = 0; j < sz/2; ++j) {
        std::cout << rotate(r1[j], r2[j]-65);
    }
    
    std::cout << std::endl;
}