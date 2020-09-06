#include <iostream>
using std::cout;
using std::endl;
using std::cin;

int main()
{
    int n, sum = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        sum += i * i;
    }
    cout << sum << endl;
    return 0;
}
