// Object는 모든 클래스의 최상위 클래스이다.

public class Archer {

  String name;
  String power;

  public Archer(String name, String power) {
    this.name = name;
    this.power = power;
  }

  public boolean equals(Object obj) { // 객체의 타입을 최상위 클래스인 Object로 지정할 수 있다.
    Archer temp = (Archer) obj;
    if (name == temp.name && power == temp.power) {
      return true;
    } else {
      return false;
    }
  }
}

public class Main {

  public static void main(String args[]) {
    Archer a1 = new Archer("궁수1", "상");
    Archer a2 = new Archer("궁수1", "상");
    System.out.println(a1.equals(a2)); // true
  }
}
