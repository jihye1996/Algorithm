import java.util.*;

public class Main{
    static ArrayList<Long> array = new ArrayList<>();

    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();
        
        if(N<=10){
            System.out.println(N);
        }else if(N>1022){
            System.out.println("-1");
        }else{
            
            for(long i=0; i<10; i++){
                descending_number(i);
            }
            Collections.sort(array);
            System.out.println(array.get(N));

        }
    }
    
    private static void descending_number(long num){
        //if(depth>10) return;
        array.add(num);
        
        for(int j=0; j<num%10; j++){
            descending_number(num*10+j);
        }
    }  
}
