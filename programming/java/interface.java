public interface Dog {
  abstract void cry();

  public void show() { // interface에서는 세부 구현을 할 수 없다.
    System.out.println("Hello");
  }
}

public interface Cat {}

// interface를 상속받을 때는 implements 키워드를 사용한다.
public class Main implements Dog, Cat { // interface는 다중 상속이 가능하다. 일반적인 class는 두 개 이상의 class를 상속받을 수 없다.

  public static void main(String args[]) {
    Main main = new Main();
    main.cry();
  }

  @Override
  public void cry() {
    System.out.println("멍멍!");
  }
}
