#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<iterator>

int main(int argc, char* argv[]) {
	int scores[5] {0};

	for (int i=0;i<5;++i) {
		std::string line;
		std::getline(std::cin, line);
		std::istringstream iss(line);
		int score = 0;
		for (int j=0;j<4;++j) {
			int x;
			iss >> x;
			score += x;
		}
		scores[i] = score;
	}	
	
	std::cout << std::distance(scores, std::max_element(scores,scores+5))+1
		<< " " 
		<< *std::max_element(scores, scores+5)
		<< '\n';
		


}
