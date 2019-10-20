#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <bitset>

struct node
{
public:
    int p = 0, q = 0;
    node(int p, int q)
    {
        this->p = p;
        this->q = q;
    }
    node(){};
};

node left(node &n) {
    return node(n.p, n.p + n.q);
}

node right(node &n) {
    return node(n.p + n.q, n.q);
}

std::ostream &operator<<(std::ostream &os, const node &n) {
    os << n.p << "/" << n.q;
    return os;
}

bool cmp(const node& a, const node& b) {
    return ((a.p==b.p) && (a.q==b.q));
}

int main(int argc, char *argv[]) {
    std::string line;
    std::getline(std::cin, line);
    int N = std::stoi(line);
   
    do {
        int d,p,q; 
        std::string pq;
        line = "4 5/2";
        std::vector<bool> bits;
        std::getline(std::cin, line);
        std::istringstream iss(line);
        iss >> d >> pq;
        p = std::stoi(pq.substr(0, pq.find("/")));
        q = std::stoi(pq.substr(pq.find("/")+1, pq.npos));
        node target = node(p,q);
        node root = node(1, 1);

        while (!cmp(target, root)) {
            if (target.q > target.p) {
                target.q-=target.p;
                bits.push_back(false);
            }
            else {
                target.p-=target.q;
                bits.push_back(true);
            }
        }

        int i = 1;
        std::reverse(bits.begin(), bits.end());
        for_each(bits.begin(), bits.end(), [&i](bool b){
            i=(i*2)+b;
        });

        std::cout << d << " " << i << std::endl;
        
       
    } while (--N > 0);
}