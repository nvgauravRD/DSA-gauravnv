#include <bits/stdc++.h>

using namespace std;

// below program returns no of digits of a number
int CoutDigits(int n){
    //Eg: log10(12) => 1.2 + 1 => floor(2.2) => 2
    return floor(log10(n) + 1);
}

int main(){
    cout<<CoutDigits(123456); // O/P : 6
    return 0;
}