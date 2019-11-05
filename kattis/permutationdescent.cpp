#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<iterator>
#include<iomanip>
#include<limits>

typedef unsigned long long descent_t;
descent_t M = 1001113;
descent_t SENTINEL = std::numeric_limits<descent_t>::max();
descent_t cache[101*100];

descent_t A(int n, int m) {
 int index = (n*100)+m;
 if (m==0 || m==n-1) cache[index]=1;
 if (cache[index] != SENTINEL) return cache[index];
 cache[index]=((n-m)*A(n-1,m-1) + (m+1)*A(n-1,m)) % M; 
 return cache[index];
}

int main(int argc, char* argv[]) {
	std::string line;
	std::getline(std::cin, line);
	int n = std::stoi(line);
	std::fill(cache, cache+(101*100), SENTINEL);
	for (int i=0;i<n;++i) {
		std::getline(std::cin,line);
		std::istringstream iss(line);
		descent_t k,N,v;
		iss >> k >> N >> v;
		descent_t p = A(N,v);	
		std::cout  << i+1 << ' ' << p << '\n'; 
	}
}
