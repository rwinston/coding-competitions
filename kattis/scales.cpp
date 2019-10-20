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
#include <iomanip>
#include <bitset>
#include <cmath>
#include <numeric>
#include <set>

//A, A#, B, C, C#, D, D#, E, F, F#, G, G#
//tone, tone, semitone, tone, tone, tone, semitone
template<typename T>
void dump(const std::set<T>& v) {
    std::for_each(v.begin(),v.end(),[](T v){std::cout << v << std::endl;});
}

std::vector<std::string> split(const std::string& s, char delimiter){
   std::vector<std::string> tokens;
   std::string token;
   std::istringstream iss(s);
   while (std::getline(iss, token, delimiter)){
      tokens.push_back(token);
   }
   return tokens;
}

int main(int argc, char* argv[]) {
   const std::string NOTES("A A# B C C# D D# E F F# G G#");
   std::vector<std::string> m = split(NOTES, ' ');
   int MAJOR_SCALE[]{2,2,1,2,2,2};  //TTSTTTS
   std::string line;
  
   std::getline(std::cin,line);
   int n = std::stoi(line);
   std::getline(std::cin,line);

   std::vector<std::string> tmp = split(line, ' ');
   std::set<std::string> piece;
   std::copy(tmp.begin(), tmp.end(), std::inserter(piece, piece.end()));
   std::set<std::string> out;
   bool fits = false;
   for (int i = 0; i < m.size(); ++i) {
      std::set<std::string> scale;
      scale.insert(m[i]);
      int interval=0;
      for (int j = 0; j < 6; ++j) {
         interval += MAJOR_SCALE[j];
         scale.insert(m[(i+interval)%12]); 
      }
      std::set<std::string> diff;
      std::set_difference(piece.begin(), piece.end(), scale.begin(), scale.end(), std::inserter(diff, diff.begin()));
      if (diff.size() == 0) {
         std::cout << m[i] << " " << std::endl;
         fits = true;
      }
   }

   if (!fits) std::cout << "none\n";
}

