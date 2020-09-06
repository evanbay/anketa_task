#include <iostream>
using std::cout;
using std::endl;
using std::cin;

// Возводит в степень
int toElevate(int num, int elv)
{
    int result = 1;
    for (int i = 1; i <= elv; i++)
    {
        result *= num;
    }
    return result;
}

int main()
{
    int x, result;
    cin >> x;
    result = toElevate(x, 16) + 10 * x - 1;
    cout << result << endl;
    return 0;
}
