#include <iostream>
using std::cout;
using std::endl;
using std::cin;

int main()
{
    int m, n, k;
    cin >> m >> n >> k;
    if (n < m) m = n;
    if (k < m) m = k;
    cout << m << endl;
    return 0;
}
