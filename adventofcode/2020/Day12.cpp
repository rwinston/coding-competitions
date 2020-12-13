#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

enum Direction { 
    E=0,S=1,W=2,N=3
};

int part1(std::vector<std::string>& commands) {
    int x = 0, y=0;
    Direction direction = Direction::E;
    for (auto command : commands) {
        int val = std::stoi(command.substr(1));
        switch (command[0]) {
            case 'N':
                y+=val;
                break;
            case 'S':
                y-=val;
                break;
            case 'E':
                x+=val;
                break;
            case 'W':
                x-=val;
                break;
            case 'R':
                direction = (Direction)((direction+(val/90)) % 4);
                break;
            case 'L': {
                int tmp = (int)direction-(val/90);
                direction = (Direction)((tmp < 0) ? tmp+4 : tmp % 4);
            }
            break;
            case 'F': {
                switch (direction) {
                    case E: x+=val; break;
                    case W: x-=val; break;
                    case N: y+=val; break;
                    case S: y-=val; break;
                }
            }
            break;
        }
    }
    return abs(x)+abs(y);
}


int main(int argc, char* argv[]) {
    std::ifstream data("c:/temp/p12.txt");
    std::vector<std::string> lines;
    std::string line;

    while (data >> line) {
        lines.push_back(line);
    }

    std::cout << part1(lines) << std::endl;
}
