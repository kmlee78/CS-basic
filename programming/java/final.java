public class Parent {

  public final void show() { // final 키워드를 사용한 메소드는 오버라이딩 할 수 없다.
    System.out.println("show");
  }
}

public class Main extends Parent {

  public static void main(String args[]) {
    final int number = 5; // final 키워드를 사용하여 변수를 상수로 선언(변경 불가)
  }
}

final class Person { // final 키워드를 사용한 class는 어떤 클래스도 상속 받을 수 없게 된다.

  String name;
  int age;
}
