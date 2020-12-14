#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <functional>

enum Direction { 
    E=0,S=1,W=2,N=3
};

const std::vector<std::function<std::pair<int,int>(int,int)>> rotations = {
                [&](int x, int y){ return std::make_pair(x, y);},      // 360R, 360L
                [&](int x, int y){ return std::make_pair(y, -x);},     // 90R, 270L
                [&](int x, int y){ return std::make_pair(-x, -y);},    // 180R, 180L
                [&](int x, int y){ return std::make_pair(-y, x);}      // 270R, 90L
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


int part2(std::vector<std::string>& commands) {
    int shipX = 0, shipY = 0;
    int wX = 10, wY = 1;
    Direction direction = Direction::E;
    for (auto command : commands) {
        int val = std::stoi(command.substr(1));
        switch (command[0]) {
            case 'N':
                wY+=val;
                break;
            case 'S':
                wY-=val;
                break;
            case 'E':
                wX+=val;
                break;
            case 'W':
                wX-=val;
                break;
            case 'R':{
                auto rotated = rotations[(val/90) % 4](wX, wY);
                wX = rotated.first; wY = rotated.second;
            }
            break;
            case 'L': {
                auto rotated =  rotations[((360-val)/90) % 4](wX, wY);
                wX = rotated.first; wY = rotated.second;
            }
            break;
            case 'F': {
               shipX += val * wX;
               shipY += val * wY;
            }
            break;
        }
        std::cout << "Ship X/Y:" << shipX << " " << shipY << " Waypoint X/Y:" << wX << " " << wY << std::endl;
    }
    return abs(shipX)+abs(shipY);
}



int main(int argc, char* argv[]) {
    std::ifstream data("c:/temp/p12.txt");
    std::vector<std::string> lines;
    std::string line;

    while (data >> line) {
        lines.push_back(line);
    }

    std::cout << part1(lines) << std::endl;
    std::cout << part2(lines) << std::endl;
}
