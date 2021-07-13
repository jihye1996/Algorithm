#include <iostream>

using namespace std;

int main()
{   
    int x[41] = {1, 0};
    int y[41] = {0, 1};
    int T, N;    
    cin >> T;

    for(int i=0; i<T; i++){
        cin >> N;
        for(int i=2; i<=N; i++){
            x[i] = x[i-2] + x[i-1];
            y[i] = y[i-2] + y[i-1];            
        }
        cout << x[N] << ' ' << y[N] << endl;
    }
   
    return 0;
}

