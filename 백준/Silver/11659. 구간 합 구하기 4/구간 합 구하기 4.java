import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // n은 숫자의 갯수, m은 연산해야 하는 횟수. n, m 선언 및 입력받기
        int n, m;

        n = sc.nextInt();
        m = sc.nextInt();

        // n개의 수 배열에 주입
        int li_1[] = new int[n];
        for (int i = 0; i < n; i++) {
            li_1[i] = sc.nextInt();
        }

        // 누적 합 배열 생성
        int prefixSum[] = new int[n + 1];
        prefixSum[0] = 0;
        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i - 1] + li_1[i - 1];
        }

        // m번의 연산
        for (int i = 0; i < m; i++) {
            int start = sc.nextInt() - 1;
            int end = sc.nextInt();

            // 누적 합 배열을 사용하여 범위 내의 합 계산
            int sum = prefixSum[end] - prefixSum[start];
            System.out.println(sum);
        }
    }
}