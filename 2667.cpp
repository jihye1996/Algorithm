#include<iostream>
#include<queue>
#include <vector>
#include<algorithm>

using namespace std;

#define MAX 25
int map[MAX][MAX];
//int visited[MAX][MAX];
int N;
vector<int> v;
int xs[4] = {0, 0, 1, -1};
int ys[4] = {1, -1, 0, 0};
int index = 2;
void bfs(int x, int y){
    int cnt = 1;
    queue<pair<int, int>> q;
    q.push(make_pair(x, y));

    while(!q.empty()){
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();
        map[cx][cy]=index;
            
        for(int i=0; i<4; i++){
            int nx = cx + xs[i];
            int ny = cy + ys[i];
            if(0<=nx && nx<N && 0<=ny && ny<N && map[nx][ny]==1){
               map[nx][ny] = index;
               //visited[nx][ny] = 1;
               cnt++; 
               q.push(make_pair(nx, ny));
            }
        }
        
    }
    v.push_back(cnt);
    index++;
    
}

int main(){
    cin >> N;
    
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            int t = 0;
            scanf("%1d", &t);
            map[i][j] = t;
        }
    }
    
    
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(map[i][j]==1) {
                bfs(i, j);
                /*
                for(int i=0; i<=N; i++){
                    for(int j=0; j<=N; j++){
                        cout << map[i][j] << ' ';
                    }
                    cout << endl;
                }   
                cout << endl;
                */
            }
        }
        
    
        
    }
    
                
    
    cout << v.size() << endl;
    sort(v.begin(), v.end());
    for(int i=0; i<v.size(); i++){
        cout << v[i] << endl;
    }
    
    return 0;
}
