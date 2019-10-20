// AdventOfCode.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

#include <filesystem>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>


static std::vector<std::string> split(const std::string& s, char delimiter) {
	std::vector<std::string> tokens;
	std::string token;
	std::istringstream tokenStream(s);
	while (std::getline(tokenStream, token, delimiter)) {
		tokens.push_back(token);
	}
	return tokens;
}

int ON = 1;
int OFF = 0;
int TOGGLE = 2;

static int toggle(bool x) {
	return (x ? false : true);
}

int main() {
	std::ifstream infile("c:/sandbox/adventofcode/2015/data/problem6_in.txt");
	std::vector<std::string> lines;

	std::string line;
	while (std::getline(infile, line)) {
		lines.push_back(line);
	}

	for (auto i = 0; i < lines.size(); ++i)
		std::cout << lines[i] << std::endl;

	bool grid[1000][1000] = { 0 };

	for (auto i = 0; i < lines.size(); ++i) {
		std::string line = lines[i];
		std::istringstream iss(line);
		std::vector<std::string> results((std::istream_iterator<std::string>(iss)),
				std::istream_iterator<std::string>());
		std::reverse(results.begin(), results.end());

		auto p1 = split(results[0], ',');
		auto p2 = split(results[2], ',');

		int x0 = atoi(p2[0].c_str());
		int y0 = atoi(p2[1].c_str());

		int x1 = atoi(p1[0].c_str());
		int y1 = atoi(p1[1].c_str());

		int code = OFF;
		if (line.find("toggle")!=std::string::npos) {
			code = TOGGLE;
		} 
		else if (line.find("on") != std::string::npos) {
			code = ON;
		}
		else if (line.find("off") != std::string::npos) {
			code = OFF;
		}

		std::cout << code << "=>" << x0 << "," << y0 << " " << x1 << "," << y1 << std::endl;

		for (int i = x0; i <= x1; ++i) {
			for (int j = y0; j <= y1; ++j) {
				if (code == ON)
					grid[i][j] = true;
				else if (code == OFF)
					grid[i][j] = false;
				else
					grid[i][j] = toggle(grid[i][j]);
			}
		}
	}

	long count=0;
	for (int i = 0; i < 1000; ++i)
		for (int j = 0; j < 1000; ++j)
			if (grid[i][j] == true)
				count++;

	std::cout << "count is " << count << std::endl;
	return 0;
}


