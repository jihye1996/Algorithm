import java.util.*;

public class Main{
    
    static int []dx = {-1,1,0,0};
    static int []dy = {0,0,-1,1};
    
    public static int BFS(int map[][], int i, int j, int n){
        int cnt = 0;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{i, j});
        map[i][j] = 2;
        
        while(!q.isEmpty()){
            int x = q.peek()[0];
            int y = q.peek()[1];
            q.poll();
            cnt++;
            
            for(int k=0; k<4; k++){
                int nx = x + dx[k];
                int ny = y + dy[k];

                if(nx >= 0 && ny >= 0 && nx < n && ny < n && map[nx][ny] == 1){
                    q.add(new int[]{nx,ny});
                    map[nx][ny] = 2;
                    
                }
            }
            
        }
        
        return cnt;
        
        
    }

     public static void main(String []args){
    	Scanner sc = new Scanner(System.in);
    	int N = sc.nextInt();
    	int home[][]  = new int[N][N];
    	
    	ArrayList<Integer> ans = new ArrayList<>();
    	
    	for(int i=0; i<N; i++){
            String str = sc.next(); 
            for(int j=0; j<N; j++){
                home[i][j] = Integer.parseInt(str.charAt(j)+"");
            }
        }
        
        sc.close();
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(home[i][j]==1){
                    ans.add(BFS(home, i, j, N));
                }
            }
        }
        
        System.out.println(ans.size());
        Collections.sort(ans);
        
        for(int i: ans){
            System.out.println(i);
        }
        
     }
}
