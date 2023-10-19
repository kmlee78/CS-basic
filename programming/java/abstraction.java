abstract class Player { // 추상 클래스

  abstract void play(string songName); // 추상 메소드

  abstract void pause();

  abstract void stop();
}

public class Main extends Player {

  public static void main(String args[]) {
    Main main = new Main();
    main.play("Hello");
    main.pause();
    main.stop();
  }

  @Override // 추상 메소드를 오버라이딩
  void play(string songName) {
    System.out.println(songName + "을 재생합니다.");
  }

  @Override
  void pause() {
    System.out.println("일시정지합니다.");
  }

  @Override
  void stop() {
    System.out.println("정지합니다.");
  }
}

// 추상 클래스를 이용한 다양한 클래스의 구현
abstract class Animal {

  abstract void cry();
}

public class Dog extends Animal {

  @Override
  void cry() {
    System.out.println("멍멍!");
  }
}

public class Cat extends Animal {

  @Override
  void cry() {
    System.out.println("야옹!");
  }
}
