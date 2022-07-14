// clang++ -Wall -std=c++14 test.cpp -o test
#include <algorithm> // for std::find
#include <iterator> // for std::begin, std::end

int main () 
{
  int a[] = {3, 6, 8, 33};
  int x = 8;
  bool exists = std::find(std::begin(a), std::end(a), x) != std::end(a);
}