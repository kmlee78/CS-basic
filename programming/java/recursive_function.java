public class Main {

  public static factorial(int number) {
    if number == 1 {
      return 1;
    } else {
      return number * factorial(number - 1);
    }
  }

  public static fibonacci(int number) {
    if number == 1 || number == 2 {
      return 1;
    } else {
      return fibonacci(number - 1) + fibonacci(number - 2);
    }
  }

  public static void main(String args[]) {
    System.out.println(factorial(5)); // 120
    System.out.println(fibonacci(10)); // 55
  }
}
