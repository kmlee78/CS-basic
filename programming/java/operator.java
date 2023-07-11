public class Main {

  public static void main(String args[]) {
    // 산술 연산자
    int a = 10;
    System.out.println(a); // 10
    a++;
    System.out.println(a); // 11
    System.out.println(++a); // 12
    System.out.println(a++); // 12
    System.out.println(a); // 13

    // 논리 연산자
    int x = 50;
    int y = 60;
    System.out.println(x == y); // false
    System.out.println(x < 30 && y > 70); // false
    System.out.println(x < 60 || y > 70); // true
    System.out.println(!(x < 60)); // false

    // 삼항 연산자
    int score = 85;
    char grade = (score > 90) ? 'A' : 'B';
    System.out.println(grade); // B

    // 제곱
    double value = Math.pow(2, 4);
    System.out.println(value); // 16.0
  }
}
