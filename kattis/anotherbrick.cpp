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


typedef struct node node;

int main(int argc, char* argv[]) {
    std::string line;
    
    std::getline(std::cin,line);
    std::istringstream iss(line);
    int h,w,n;
    iss >> h >> w >> n;

    std::getline(std::cin,line);
    std::istringstream iss(line);
    int* bricks = new int[n];
    for (int i=0;i<n;++i) {
        iss >> bricks[i];
    }

    // bricks / line = width/brckwidth
    // height = bricks/(bricks/line)
    int thisline=w,lines=0;
    for (int i=0;i<n;++i){
        thisline-=bricks[i];
        if (thisline==0) {
            lines++; thisline=w;
        }
        if(thisline<0) break;
    }

    std::cout << ((lines<h)? "NO":"YES") << std::endl;    
}
