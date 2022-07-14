// clang++ -Wall -std=c++14 ccc12s2.cpp -o ccc12s2
#include <iostream>
#include <string>
using namespace std;

int rom_dec(char rom_num) {
    char rom_nums[7] = {'I','V','X','L','C','D','M'};
    int dec_nums[7] = {1,5,10,50,100,500,1000};
   
    for (int i = 0; i < 7; i++) {
        if (rom_nums[i] == rom_num) {
            return dec_nums[i];
        }
    }
    return 0;
}

int ara_dec(char ara_dec) {
    char ara_decs[9] = {'1','2','3','4','5','6','7','8','9'};
    int dec_nums[9] = {};

    for (int i = 1; i < 10; i++) {
        dec_nums[i-1] = i;
    }
   
    for (int i = 0; i < 9; i++) {
        if (ara_decs[i] == ara_dec) {
            return dec_nums[i];
        }
    }
    return 0;
}

int main() {

    string aro_num;
    cin >> aro_num;

    int aro_tot = 0;

    for (int i = 0; i < aro_num.length(); i += 2) {
        if (rom_dec(aro_num[i+1]) >= rom_dec(aro_num[i+3])) {
            aro_tot += ara_dec(aro_num[i]) * rom_dec(aro_num[i+1]);
        }
        else {
            aro_tot -= ara_dec(aro_num[i]) * rom_dec(aro_num[i+1]);
        }
       
        // cout << rom_dec(aro_num[i+1]) << " " << rom_dec(aro_num[i+3]) << " " << aro_tot << endl;
    }

    cout << aro_tot << endl;

    return 0;
}