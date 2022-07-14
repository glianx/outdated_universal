// CCC '10 S2 - Huffman Encoding
// clang++ -Wall -std=c++11 ccc10s2.cpp -o ccc10s2
#include <iostream>
#include <string>
using namespace std;

int found(string element, string* array, int array_len);

int main() {
    int k;
    cin >> k;

    char char_array[20];
    string bin_array[20];

    for (int i = 0; i < k; i++) {
        char _char;
        cin >> _char;

        // set ith index of char_array as input character
        char_array[i] = _char;

        string bin_number;
        cin >> bin_number;

        // set ith index of char_array as input binary number (as string)
        bin_array[i] = bin_number;
    }

    // for (int i = 0; i < k; i++) {
    //     cout << endl << char_array[i] << " " << bin_array[i];
    // }

    string bin_sequence;
    cin >> bin_sequence;

    // iterate over binary sequence with pos, len variables
    // if match not found, len = len + 1
    // if match found, pos = pos + len, len = 1

    int pos = 0;
    int len = 1;

    int str_len = bin_sequence.length();
    int arr_len = sizeof(bin_array) / sizeof(bin_array[0]);

    // cout << endl << str_len;

    // cout << endl << bin_array[4] << endl;
    // cout << endl << found("111", bin_array, sizeof(bin_array) / sizeof(bin_array[0]));

    while (pos < str_len) {
        string substr = bin_sequence.substr(pos, len);
        int index = found(substr, bin_array, arr_len);

        // if code found, then print corresponding letter
        if (index != -1) {
            cout << char_array[index];

            // shift position to next "block" and reset len to zero
            pos = pos + len;
            len = 1;
        }

        // if code not found, then iterate size of block
        else {
            len = len + 1;
        }
        
        // cout << endl << pos << " " << len;
    }

}

int found(string element, string* array, int array_len) {
    for (int i = 0; i < array_len; i++) {
        if (array[i] == element) {
            return i;
        }
    }
    return -1;
}