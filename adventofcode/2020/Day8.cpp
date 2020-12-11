#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

enum class Instruction : int {
    NOP, ACC, JMP
};

Instruction convert(const std::string& str) {
    if (str == "acc") return Instruction::ACC;
    else if(str == "jmp") return Instruction::JMP;
    else return Instruction::NOP;
}

bool run(const std::vector<std::pair<Instruction, int>>& instructions, std::vector<bool> executed) {
    int pc = 0, acc = 0;  
    while (pc < instructions.size() && !executed[pc]) {
        auto instruction = instructions[pc];
        executed[pc] = true;

        switch(instruction.first) {
            case Instruction::NOP:
                pc++;
                break;
            case Instruction::JMP:
                pc = pc + instruction.second;
                break;
            case Instruction::ACC:
                acc += instruction.second;
                pc++;
                break;
        }          
    }
    std::cout << "[END] pc=" << pc << ", acc=" << acc << "\n";
    return executed[pc];
}

int main(int argc, char* argv[]) {
    std::ifstream data("c:/temp/p8");
    std::string ins;
    int count;
    std::vector<std::pair<Instruction, int>> instructions;
    std::vector<bool> executed;
    while (data >> ins >> count) {
        std::cout << ins << " " << count << std::endl;
        instructions.push_back(std::make_pair(convert(ins), count));
        executed.push_back(false);
    }
    
    int i = 0;
    for (int i =0; i < instructions.size(); ++i) {
        Instruction opcode = instructions[i].first;
        instructions[i].first = (opcode ==  Instruction::JMP ? Instruction::NOP : opcode==Instruction::NOP ? Instruction::JMP : opcode);
        bool loop = run(instructions, executed);
        if (!loop) {
            std::cout << " Found non-looping solution\n";
            return 0;
        }
        instructions[i].first = opcode;
    }

    std::cout << "No solution found\n";
}
