#include<iostream>
using namespace std;
int main(){
    unsigned long long r = 1;
    int n; cin >> n;
    for(int i = 1; i <= n; i++){
        r*=i;
    }
    cout << r;
    return 0;
}