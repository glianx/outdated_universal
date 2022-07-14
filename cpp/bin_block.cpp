// clang++ -Wall -std=c++14 bin_block.cpp -o bin_block
#include <iostream>
using namespace std;

int bin_block(long int face, int i) {
    // return (face >> (7 - i) * 8) & ((1 << 8) - 1);
    // return (face & (((1 << 8) - 1) << ((7 - i) * 8))) >> ((7 - i) * 8);
    long long int block = (1 << 8) - 1;
    return block << 24;
}

int main() {
    long int f = 217020518514230019;
    long long int sticker = bin_block(f,2);
    cout << sticker << endl;
    
    string binary = bitset<64>(sticker).to_string();
    cout<<binary<<"\n";
    return 0;
}