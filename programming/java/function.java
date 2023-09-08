public class Main {

  // 반환형, 함수명, 매개변수로 사용자 정의 함수 선언
  public static int function(int number, int k) {
    for (int i = 1; i <= number; i++) {
      if (numer % i == 0) {
        k--;
        if (k == 0) {
          return i;
        }
      }
    }
    return -1;
  }

  // 문자열의 마지막 문자를 반환하는 함수
  public static char function2(String input) {
    return input.charAt(input.length() - 1);
  }

  public static void main(String args[]) {
    // k번째 약수 구하기
    int result = function(3050, 10);
    if (result != -1) {
      System.out.println(result); // 610
    } else {
      System.out.println("3050의 10번째 약수는 없습니다.");
    }

    // 문자열의 마지막 문자 출력
    char result2 = function2("Hello World");
    System.out.println(result2); // d
  }
}
