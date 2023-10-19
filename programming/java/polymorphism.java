public class Fruit {

  String name;
  int price;

  public void show() {
    System.out.println(name);
    System.out.println(price);
  }
}

public class Apple extends Fruit {

  public Apple() {
    name = "사과";
    price = 1000;
  }
}

public class Banana extends Fruit {

  public Banana() {
    name = "바나나";
    price = 2000;
  }
}

public class Main {

  public static void main(String args[]) {
    Fruit fruit = new Apple();
    fruit.show(); // 사과, 1000

    Fruit fruit2 = new Banana();
    fruit2.show(); // 바나나, 2000
  }
}
