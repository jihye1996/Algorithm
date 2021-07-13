#include <iostream>

using namespace std;

int main()
{   
    int v[1000001] ={0, 0, 1, 1};
    int N;   
    cin >> N;

    for(int i=4; i<=N; i++){
        v[i] = v[i-1]+1;
      
        if(i%3==0){
            if(v[i])
            v[i] = min(v[i], v[i/3]+1);
        }
        if(i%2==0){
            v[i] = min(v[i], v[i/2]+1);
        }
    }
    
    cout << v[N]<< endl;
   
    return 0;
}
