import java.util.*;

public class Main {


	public static void main(String[] args) {
        
		// n을 입력받고
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int R = 0;
		for (int i = 1; i < N; i++) {
            String str = String.valueOf(i);
            int sum = i;
            for (int j = 0; j < str.length(); j++) {
			    sum += str.charAt(j) - '0';
		    }

			if (sum==N) {
				R = i; // 그 경우에 생성자는 i
				break;
			}
		}
		System.out.println(R); // 정답 출력
    sc.close();
	}

}
