import java.io.File;
import java.util.Scanner;

public class Main {

  public static void main(String args[]) {
    // 콘솔 입출력
    Scanner sc = new Scanner(System.in); // 콘솔창 입력을 위한 Scanner 객체 생성
    System.out.print("숫자를 입력하세요: ");
    int i = sc.nextInt(); // 사용자가 입력한 숫자를 읽어들임
    System.out.println(i);
    sc.close(); // Scanner 객체 닫기

    // 파일 입출력
    File file = new File("input.txt"); // 파일 객체 생성
    try {
      Scanner sc2 = new Scanner(file); // 파일로부터 읽어들임
      while (sc2.hasNextInt()) { // 파일의 끝까지 읽어들임
        System.out.println(sc2.nextInt()); // 파일의 내용을 출력
      }
      sc2.close(); // Scanner 객체 닫기
    } catch (FileNotFoundException e) {
      System.out.println("파일을 찾을 수 없습니다.");
    }
  }
}
