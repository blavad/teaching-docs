#include <iostream>

using namespace std;

int main()
{
    cout << "Partie 1" << std::endl;

    int p1 = 10;
    int *p2 = &p1;

    cout << p1 << std::endl;

    *p2 += 10;
    cout << p1 << std::endl;

    cout << "Partie 2" << std::endl;

    int tab[3] = {1, 2, 3};
    int *p3 = tab;

    cout << tab[0] << tab[1] << tab[2] << std::endl;
    cout << *p3 << std::endl;

    *(p3 + 1) = 10;
    cout << tab[0] << tab[1] << tab[2] << std::endl;
    cout << tab[1] << std::endl;
    cout << *(p3 + 2) << std::endl;
}
