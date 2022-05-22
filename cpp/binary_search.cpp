// clang++ -Wall -std=c++11 sort.cpp -o sort
#include <iostream>
using namespace std;

int main() {
    int arr[8] = {5,3,11,6,0,8,1,9};
    len_arr = sizeof(arr) / sizeof(int)
    for (int i = len_arr - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;

                for (int i = 0; i < len_arr; i++) {
                    cout << arr[i] << " ";
                }
                cout << "\t" << i << " " << j << endl;
            }
        }
    }
    return 0;
}