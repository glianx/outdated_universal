// clang++ -Wall -std=c++11 q.cpp -o q
#include <iostream>
#include <queue>
using namespace std;

void showq(queue<int> q) {
    queue<int> p = q;

    cout << p.empty() << endl;
    cout << p.size() << endl;
    cout << p.front() << endl;
    cout << p.back() << endl;

    while (!p.empty()) {
        cout << p.front() << " ";
        p.pop();
    }
    cout << "\n";
}

int main() {
    queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);

    showq(q);
    
    q.pop();
    q.pop();

    showq(q);

    return 0;
}