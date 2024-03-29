
>💡 프로그래밍 패러다임(programming paradigm)은 프로그래머에게 프로그래밍의 관점을 갖게 해주는 역할을 하는 개발 방법론이다.
>

![image](https://user-images.githubusercontent.com/72758925/233765216-bd510bc7-bc9d-45c8-9301-d03bb9432f74.png)

[1. 선언형과 함수형 프로그래밍](#1-선언형과-함수형-프로그래밍)\
[2. 객체지향 프로그래밍](#2-객체지향-프로그래밍)\
[3. 절차형 프로그래밍](#3-절차형-프로그래밍)\
[4. 패러다임의 혼합](#4-패러다임의-혼합)

# 1. 선언형과 함수형 프로그래밍

**<선언형 프로그래밍>**

- ‘무엇을’ 풀어내는가에 집중하는 패러다임이며, “프로그램은 함수로 이루어진 것이다.”라는 명제가 담겨 있는 패러다임

**<함수형 프로그래밍>**

- 함수형 패러다임은 선언형 패러다임의 일종임.
- 작은 ‘순수 함수’들을 블록처럼 쌓아 로직을 구현하고 ‘고차 함수’를 통해 재사용성을 높인 프로그래밍 패러다임
- 자바스크립트는 함수가 일급 객체이기 때문에 객체지향형 프로그래밍 보다는 함수형 프로그래밍 방식이 선호된다.

**순수 함수**: 반환값이 오직 들어오는 인자에만 영향을 받는 함수

**고차 함수**: 함수를 매개변수로 받아 로직을 생성할 수 있는 함수

### 일급 객체

일급 객체의 특징은 다음과 같다.

- 변수나 메서드에 함수를 할당할 수 있다.
- 함수 안에 함수를 매개변수로 담을 수 있다.
- 함수가 함수를 반환할 수 있다.

---

# 2. 객체지향 프로그래밍

>객체들의 집합으로 프로그램의 상호 작용을 표현하며 데이터를 객체로 취급하여 객체 내부에 선언된 메서드를 활용하는 방식의 프로그래밍
>

- 설계에 많은 시간이 소요되며, 처리 속도가 다른 프로그래밍 패러다임에 비해 상대적으로 느림

### 객체지향 프로그래밍의 특징

- 추상화: 복잡한 시스템으로부터 핵심적인 개념 또는 기능을 간추려내는 것을 의미
- 캡슐화: 객체의 속성과 메서드를 하나로 묶고 일부를 외부에 감추어 은닉하는 것을 의미
- 상속성: 상위 클래스의 특성을 하위 클래스가 이어받아서 재사용하거나 추가, 확장하는 것을 의미. 클래스의 계층 관계 형성이나 코드의 재사용성, 유지 보수성 측면에서 중요함
- 다형성: 하나의 메서드나 클래스가 다양한 방법으로 동작하는 것을 의미. 대표적으로 오버로딩과 오버라이딩이 있음
- 오버로딩: 같은 이름을 가진 메서드를 여러 개 두는 것을 뜻함. 메서드의 타입, 매개변수의 유형, 개수 등으로 여러 개를 둘 수 있다.
- 오버라이딩: 상위 클래스로부터 상속받은 메서드를 하위 클래스가 재정의하는 것을 의미

### 설계 원칙

- 단일 책임 원칙(SRP, Single Responsibility Principle): 모든 클래스는 각각 하나의 책임만 가져야 하는 원칙
- 개방-폐쇄 원칙(OCP, Open Closed Principle): 유지 보수 사항이 생긴다면 코드를 쉽게 확장할 수 있도록 하고 수정할 때는 닫혀 있어야 하는 원칙
- 리스코프 치환 원칙(LSP, Liskov Substitution Principle): 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 하는 것을 의미. 부모 객체에 자식 객체를 넣어도 시스템이 문제없이 돌아가야 함
- 인터페이스 분리 원칙(ISP. Interface Segregation Principle): 하나의 일반적인 인터페이스보다 구체적인 여러 개의 인터페이스를 만들어야 하는 원칙
- 의존 역전 원칙(DIP, Dependency Inversion Principle): 자신보다 변하기 쉬운 것에 의존하던 것을 추상화된 인터페이스나 상위 클래스를 두어 변하기 쉬운 것의 변화에 영향받지 않게 하는 원칙

---

# 3. 절차형 프로그래밍

> 로직이 수행되어야 할 연속적인 계산 과정으로만 이루어진 프로그래밍
> 
- 코드의 가독성이 좋으며 실행속도가 빠름
- 모듈화하기가 어렵고, 유지 보수성이 떨어짐

---

# 4. 패러다임의 혼합

- 비즈니스 로직이나 서비스의 특징을 고려해서 패러다임을 정하는 것이 좋음
- 예를 들어 백엔드에 머신 러닝 파이프라인과 거래 관련 로직이 있다면 머신 러닝 파이프라인은 절차지향형 패러다임, 거래관련 로직은 함수형 프로그래밍을 적용하는 것이 좋겠지