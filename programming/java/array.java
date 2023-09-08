import java.util.Scanner;

public class Main {

  public static int max(int a, int b) {
    return a > b ? a : b;
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("배열의 크기를 입력하세요: ");
    int n = scanner.nextInt();
    int[] array = new int[n];
    for (int i = 0; i < n; i++) {
      System.out.print("배열의 " + (i + 1) + "번째 원소를 입력하세요: ");
      array[i] = scanner.nextInt();
    }
    int result = array[0];
    for (int i = 1; i < n; i++) {
      result = max(result, array[i]);
    }
    System.out.println("배열의 최댓값은 " + result + "입니다.");

    // 다차원 배열
    int N = 50;
    int[][] array2 = new int[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        array2[i][j] = (int) (Math.random() * 10); // 형변환
      }
    }
    System.out.println(array2[0][0]); // 0행 0열
    System.out.println(array2[0][1]); // 0행 1열
  }
}
