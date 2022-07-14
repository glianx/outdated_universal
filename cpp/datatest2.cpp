// clang++ -Wall -std=c++14 datatest2.cpp -o datatest2
#include <iostream>
#include <bitset>
#include <string>
#include <cmath>

using namespace std;
void render(long int bin_cube[6]);

long int get_bin_face(long int x) {
    long int bin_face = 0;
    for (long int i = 0; i < 8; i++) {
        bin_face += (x << i * 8);
    }
    return bin_face;
}

long int * get_bin_cube() {
    static long int bin_cube[6];
    for (long int x = 0; x < 7; x++) {
        long int bin_face = get_bin_face(x);
        bin_cube[x] = bin_face;

        string binary = bitset<64>(bin_cube[x]).to_string();

        cout << binary << endl;
        cout << bin_cube[x] << endl;
    }

    return bin_cube;
}

long int get_cw_rot_bin_face(long int bin_face) {
    return (bin_face << 48) | (bin_face >> 16);
}

long int get_ccw_rot_bin_face(long int bin_face) {
    return (bin_face << 16) | (bin_face >> 48);
}

long int * get_umove_cube(long int bin_cube[6]) {
    bin_cube[0] = get_cw_rot_bin_face(bin_cube[0]);

    long int temp_face = (bin_cube[4] & ((1L << 40) - 1)) | (bin_cube[1] & ((1L << 24) - 1) << 40);
    for (int i = 1; i < 4; i++) {
        bin_cube[i] = (bin_cube[i] & ((1L << 40) - 1)) | (bin_cube[i+1] & ((1L << 24) - 1) << 40);
    }
    bin_cube[4] = temp_face;
    return bin_cube;
}

long int * get_rmove_cube(long int bin_cube[6]) {
    bin_cube[3] = get_cw_rot_bin_face(bin_cube[3]);

    long int temp_face = (bin_cube[4] & (((1L << 40) - 1) << 16)) | ((((bin_cube[0] >> 24) & ((1 << 8) - 1)) << 56) | ((bin_cube[0] >> 32) & ((1 << 16) - 1)));

    bin_cube[0] = (bin_cube[0] & (~(((1L << 24) - 1) << 24))) | (bin_cube[2] & (((1L << 24) - 1) << 24));
    bin_cube[2] = (bin_cube[2] & (~(((1L << 24) - 1) << 24))) | (bin_cube[5] & (((1L << 24) - 1) << 24));
    bin_cube[5] = (bin_cube[4] & (((1L << 40) - 1) << 16)) | ((((bin_cube[5] >> 24) & ((1 << 8) - 1)) << 56) | ((bin_cube[5] >> 32) & ((1 << 16) - 1)));

    bin_cube[4] = temp_face;

    return bin_cube;
}

int get_sticker(long int face, int i) {
    long int block = (1 << 8) - 1;
    return (face & (block << (7 - i) * 8)) >> ((7 - i) * 8);
}

void render(long int bin_cube[6]) {
    string colrs[7] = {"🟨","🟧","🟦","🟥","🟩","⬜️","  "};
    int facerows[3][4] = {{6,0,6,6},{1,2,3,4},{6,5,6,6}};
    int rows[3][3] = {{0,1,2},{7,8,3},{6,5,4}};
    for (int facerow = 0; facerow < 3; facerow++) {
        for (int row = 0; row < 3; row++) {
            for (int face = 0; face < 4; face++) {
                for (int column = 0; column < 3; column++) {
                    if (rows[row][column] != 8) {
                        cout << colrs[get_sticker(bin_cube[facerows[facerow][face]],rows[row][column])];
                    }
                    else {
                        cout << colrs[facerows[facerow][face]];
                    }
                }
            }
            cout << endl;
        }
    }
    cout << endl;
}

int main()
{
    long int *bin_cube_ptr;
    bin_cube_ptr = get_bin_cube();
    render(bin_cube_ptr);

    bin_cube_ptr = get_umove_cube(bin_cube_ptr);
    render(bin_cube_ptr);

    bin_cube_ptr = get_rmove_cube(bin_cube_ptr);
    render(bin_cube_ptr);

    bin_cube_ptr = get_rmove_cube(bin_cube_ptr);
    render(bin_cube_ptr);

    for (long int x = 0; x < 7; x++) {
        string binary = bitset<64>(*(bin_cube_ptr + x)).to_string();

        cout << binary << endl;
        cout << *(bin_cube_ptr + x) << endl;
    }

    return 0;
}