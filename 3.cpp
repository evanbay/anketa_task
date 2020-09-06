#include <iostream>
using std::cout;
using std::endl;
using std::cin;

int main()
{
    int n;
    cin >> n;
    while (n > 0) {
        cout << n % 10;
        n /= 10;
    }
    cout << endl;
    return 0;
}
