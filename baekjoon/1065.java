import java.util.*;

public class Main{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
      
        int N = sc.nextInt();
        sc.close();
          
        int answer = 0;
          
        if(N<100){
            answer = N;    
        }else{
            answer = 99;
            if(N==1000) N=999;
            for(int i=100; i<=N; i++){
                int one, two, three;
                one = i/100;
                two = (i/10)%10;
                three = i%10;
                
                if((one-two) == (two-three)){
                    answer++;
                }
            }
                  
        }
        System.out.println(answer);
    }
}
