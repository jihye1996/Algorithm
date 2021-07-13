#include <iostream>

using namespace std;

int main()
{   
    int x[10] = {1, 2, 4};
    int T, N;    
    cin >> T;

    for(int i=0; i<T; i++){
        cin >> N;
        for(int i=3; i<N; i++){
            x[i] = x[i-3] + x[i-2] + x[i-1];         
        }
        cout << x[N-1]<< endl;
    }
   
    return 0;
}

