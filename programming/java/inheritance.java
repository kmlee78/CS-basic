public class Person {

  private String name;
  private int age;
  private int height;
  private int weight;

  // get, set 메소드 생략
  public Person(String name, int age, int height, int weight) {
    this.name = name;
    this.age = age;
    this.height = height;
    this.weight = weight;
  }
  public void getInfo() {
    System.out.println(this.name + " " + this.age + " " + this.height + " " + this.weight)
  }
}

public class Student extends Person { // Person 클래스를 상속받는 Student 클래스

  private String studentID;
  private int grade;
  private double GPA;

  public Student(
    String name,
    int age,
    int height,
    int weight,
    String studentID,
    int grade,
    double GPA
  ) {
    super(name, age, height, weight); // super 키워드로 부모 클래스의 생성자 호출
    this.studentID = studentID;
    this.grade = grade;
    this.GPA = GPA;
  }

  public void show() {
    getInfo(); //부모 클래스의 메소드 호출
    System.out.println(this.studentID + " " + this.grade + " " + this.GPA);
  }
}

public class Teacher extends Person{
    private String teacherID;
    private int monthSalary;
    private int workedYear;
    // 생성자, get, set 메소드 생략
    public show(){
        getInfo();
        System.out.println(this.teacherID + " " + this.monthSalary + " " + this.workedYear);
    }
}

public class Main {

  public static void main(String args[]) {
    Student student = new Student("홍길동", 20, 175, 70, "20200001", 1, 4.5);
    student.show(); // 홍길동 20 175 70 20200001 1 4.5

    // Person 클래스의 인스턴스 배열 생성
    Student[] students = new Student[10];
    for (int i = 0; i < 10; i++) {
      students[i] = new Student("홍길동", 20, 175, 70, i + "", 1, 4.5);
    }

    // 학생 정보를 입력받아서 인스턴스 배열 생성
    Scanner scanner = new Scanner(System.in);
    System.out.print("학생의 수: ");
    int n = scanner.nextInt();
    Student[] students = new Student[n];
    for (int i = 0; i < n; i++) {
      System.out.print("학생의 이름, 나이, 키, 몸무게, 학번, 학년, 학점: ");
      students[i] = new Student(
        scanner.next(),
        scanner.nextInt(),
        scanner.nextInt(),
        scanner.nextInt(),
        scanner.next(),
        scanner.nextInt(),
        scanner.nextDouble()
      );
    }
    for (int i = 0; i < n; i++) {
      students[i].show();
    }
    scanner.close();
  }
}
