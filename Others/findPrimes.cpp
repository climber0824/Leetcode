#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int num) {
    if (num == 2) return true;
    if (num%2==0 || num < 2) return false;
    else {
        for (int i=3; i*i<=num; i+=2) {
            if (num%i == 0) {
                return false;
            }
        }
        return true;
    }
}


int main() {
    // Write C++ code here
    int n=17;
    for (int i=3; i<=n; i++) {
        if (isPrime(i)) cout<<i<<endl;
    }
    return 0;
}
