public class Main {

  static final double PI = 3.14; // 상수 선언

  public static void main(String args[]) {
    // 변수 선언
    int intType = 100;
    double doubleType = 100.5;
    String stringType = "Hello World";

    // 출력
    System.out.println(intType); // 자동 줄바꿈
    System.out.print(PI); // 줄바꿈 없음, 상수 출력

    // 오버플로우 발생
    int a = 2147483647;
    System.out.println(a + 1); // -2147483648

    // 실수를 정수형으로 변환
    int a = (int) 3.14; // 3
  }
}
