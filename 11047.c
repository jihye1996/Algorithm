#include<iostream>

using namespace std;

#define MAX 10

int main(){
    
    int n, cash, sum=0;
    int coins[MAX] = {};
    
    cin >> n >> cash;

    for(int i=0; i<n; i++) cin >> coins[i];
    
    for(int i=n-1; 0<=i; i--){
        sum += cash/coins[i];
        cash %= coins[i];
    }
    
    cout << sum;
    
    
    return 0;
}
