#include<iostream>
using namespace std;

//Lower Triangle
int main() {
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}


// Upper Triangle
int main() {
    int rows = 5;

    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < i; j++) {
            cout << "  ";
        }
        for(int j = rows; j > i; j--) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}


 // Pyramid Pattern containing '*' 
int main() {
    int n = 5;

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n - i; j++) {
            cout << "  ";
        }
        for(int j = 1; j <= 2 * i - 1; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
