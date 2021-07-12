#include<iostream>
#include<queue>
using namespace std;

#define MAX 101

int map[MAX][MAX];
//int visited[MAX][MAX];
int N, M;
int xs[4] = {0, 0, -1, 1}; //row
int ys[4] = {-1, 1, 0, 0}; //col

void bfs(int x, int y){
    queue<pair<int, int>> q;
    q.push(make_pair(x, y));
    //visited[x][y] = 1;
    
    while(!q.empty()){
        int cur_x = q.front().first;
        int cur_y = q.front().second;
        //int cur = map[cur_x][cur_y];
        q.pop();
        
        for(int i=0; i<4; i++){
            int next_x = xs[i]+cur_x;
            int next_y = ys[i]+cur_y;
            // if map is not 1, then already visit
            if(1<= next_x  && next_x<= N && 1<= next_y && next_y <= M && map[next_x][next_y] == 1){
               
                q.push(make_pair(next_x, next_y));
                map[next_x][next_y] = map[cur_x][cur_y]+1;
                //visited[next_x][next_y] = 1;
                
            }
            
        }

        
    }
}

int main(){
    
    cin >> N >> M;
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=M; j++){
            int t;
            scanf("%1d", &t);
            map[i][j] = t;
            //cout << map[i][j];
        }
        //cout << endl;
    }
    
    bfs(1, 1);
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=M; j++){
            
            cout << map[i][j] << ' ';
        }
        cout << endl;
    }
    
    cout << map[N][M];
    
    return 0;
}
