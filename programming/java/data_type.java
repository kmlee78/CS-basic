public class Main {

  public static void main(String args[]) {
    // a부터 z까지 출력. ASCII 코드 사용
    for (char i = 'a'; i <= 'z'; i++) {
      System.out.print(i); // abcdefghijklmnopqrstuvwxyz
    }

    // 10진수를 8진수, 16진수로 출력
    int a = 100;
    System.out.format("%o\n", a); // 144
    System.out.format("%x\n", a); // 64

    // 문자열 활용
    String name = "John";
    System.out.println(name.substring(1, 3)); // oh. 1번 인덱스부터 3번 인덱스 전까지 출력
  }
}
