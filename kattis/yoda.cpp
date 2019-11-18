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

int max(int a, int b) { return (a<b)?b:a; }

typedef struct node node;

int main(int argc, char* argv[]) {
    std::string line;
    std::getline(std::cin,line);
    int n = std::stoi(line);
    std::getline(std::cin,line);
    int p = std::stoi(line);
    //   int n=2341,p=6785;
    int nd = (int)floor(log10(n))+1;
    int np = (int)floor(log10(p))+1;

    int maxd = (int)std::max(nd,np);
    std::stringstream ss;
    ss << n;
    std::string ns = ss.str();

    std::stringstream ss2;
    ss2 << p;
    std::string ps = ss2.str();
    
    std::reverse(ns.begin(), ns.end());
    std::reverse(ps.begin(), ps.end());

    std::string ny,py;
    for (int i=0;i<maxd;++i){
        int ndig = (i>=nd)?0:((int)ns[i]-'0');
        int pdig = (i>=np)?0:((int)ps[i]-'0');
        if (i>=ps.length() || ns[i]>ps[i]) {
            ny+=ns[i];
        } else if (i>=ns.length() || ps[i]>ns[i]){
            py+=ps[i];
        } else{ py+=ps[i];ny+=ns[i];}
    }

    std::reverse(py.begin(), py.end());
    std::reverse(ny.begin(), ny.end());
    if(ny.size()==0) std::cout << "YODA\n";
    else {     n=std::stoi(ny);std::cout << n << std::endl;}
    if(py.size()==0) std::cout << "YODA\n";
    else {     p=std::stoi(py);std::cout << p << std::endl;}
    
}
