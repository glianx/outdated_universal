// clang++ -Wall -std=c++14 datatest.cpp -o datatest
#include <iostream>
#include <bitset>
#include <string>
using namespace std;

long int get_bin_face(long int x) {
    long int bin_face = 0;
    for (int i = 0; i < 8; i++) {
        bin_face += (x << i * 8);
    }
    return bin_face;
}

// void render(long int bin_cube[6]) {
//     string colrs[7] = {"🟨","🟧","🟦","🟥","🟩","⬜️","  "};
//     int facerows[3][4] = {{6,0,6,6},{1,2,3,4},{6,5,6,6}};
//     int rows[3][3] = {{0,1,2},{7,0,3},{6,5,4}}; // *note center sticker
//     for (int facerow = 0; facerow < 3; facerow++) {
//         for (int row = 0; row < 3; row++) {
//             for (int face = 0; face < 4; face++) {
//                 for (int column = 0; column < 3; column++) {
//                     // cout << colrs[facerows[facerow][face]];
//                     cout << colrs[bin_cube[facerow+face][face]];
//                 }
//             }
//             cout << endl;
//         }
//     }
// }

// 6 0 6 6
// 1 2 3 4
// 6 5 6 6

int main()
{
    long int bin_cube[6];

    for (long int x = 0; x < 6; x++) {
        long int bin_face = get_bin_face(x);
        bin_cube[x] = bin_face;

        string binary = bitset<64>(bin_cube[x]).to_string();
        cout<<binary<<"\n";
        cout<<bin_cube[x]<<"\n";

    }

    // render(bin_cube);

    return 0;
}