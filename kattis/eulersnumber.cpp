#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<iterator>
#include<iomanip>

int main(int argc, char* argv[]) {
	std::string line;
	std::getline(std::cin, line);
	int n = std::stoi(line);
	double e = 1.0;
	double fact = e;
	for (int i = 1; i <=n; ++i) {
		fact*=i;
		e+=(1.0/fact);
	}
	std::cout << std::setprecision(15) << e << '\n';

}
