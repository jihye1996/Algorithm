#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int N;
    int M[1001] = {0, 1, 2};
    cin >> N;
    
    for(int i=3; i<=N; i++){
        M[i] = (M[i-1] + M[i-2])%10007;
    }

    cout << M[N];
    
    return 0;
}
