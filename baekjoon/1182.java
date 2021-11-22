import java.util.*;
import java.io.*;

public class Main {
    static int N, S, C;
    static int[] nums;
    
    static void backTracking(int c_sum, int index){
        if(S==c_sum) C++;
        
        for(int i=index; i<N; i++){
            backTracking(c_sum+nums[i], i+1);
        }
    }
    
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        S = sc.nextInt();
        nums = new int[N];
        
        for(int i=0;i<N;i++ ) {
            nums[i] = sc.nextInt();
        }

        sc.close();
        
        for(int i=0;i<N;i++ ) {
            backTracking(nums[i], i+1);
        }
        
        System.out.println(C);

    }
}
