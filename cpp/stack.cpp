#include <iostream>
#include <stack>

using namespace std;

void showstk(stack<int> stk) {
    stack<int> stk2 = stk;
    cout << stk2.empty() << endl;
    cout << stk2.size() << endl;
    cout << stk2.top() << endl;

    while (!stk2.empty()) {
        cout << stk2.top() << " ";
        stk2.pop();
    }

    cout << "\n";
}

int main() {
    stack<int> stk;
    stk.push(1);
    stk.push(2);
    stk.push(3);

    showstk(stk);

    stk.pop();
    stk.pop();

    showstk(stk);
}