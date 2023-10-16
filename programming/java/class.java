public class Node {

  private int x; // private 접근 제한자. 클래스 내부에서만 접근 가능
  private int y;

  public int getX() { // public 접근 제한자. 클래스 외부에서도 접근 가능
    return x;
  }

  public void setX(int x) {
    this.x = x;
  }

  public int getY() {
    return y;
  }

  public void setY(int y) {
    this.y = y;
  }

  public Node(int x, int y) { // 생성자. 동일한 이름을 가진 메소드. 반환형이 없다.
    this.x = x;
    this.y = y;
  }

  public Node getCenter(Node other) { // 다른 노드와의 중간 좌표를 구하는 메소드
    return new Node((this.x + other.getX()) / 2, (this.y + other.getY()) / 2);
  }
}

public class Main {

  public static void main(String args[]) {
    Node one = new Node(10, 20); // Node 클래스의 인스턴스 생성
    Node two = new Node(30, 40);
    Node center = one.getCenter(two); // 중간 좌표를 구하는 메소드 호출
    System.out.println("(" + center.getX() + ", " + center.getY() + ")"); // (20, 30)
  }
}
