#include <bits/stdc++.h>

using namespace std;

// function returns sum of digits
int sumOfDigits(int n){
    int sum = 0;

    // looping through each digit
    while (n != 0){
        sum += (n%10); // 1 + 2 + 3
        n /= 10;
    }

    return sum // 1+2+3 = 6
}
int main(){
    cout<<sumOfDigits(123);// O/P: 6
    return 0;
}