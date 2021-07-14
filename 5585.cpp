#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int N, C = 0;
    int M[6] = {500, 100, 50, 10, 5, 1};
    cin >> N;
    
    N = 1000 - N;
    
    for(int i=0; i<6; i++){
        if(N%M[i] == 0){
            C += (int)N/M[i];
            break;
        }else{
            C += (int)N/M[i];
            N = N%M[i];
        }    
    }
    
    
    cout << C;
    
    return 0;
}
