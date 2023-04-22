>💡 조인(join)이란 하나의 테이블이 아닌 두 개 이상의 테이블을 묶어서 하나의 결과물을 만드는 것을 말한다.


MySQL 에서는 JOIN 이라는 쿼리로, MongoDB 에서는 lookup이라는 쿼리로 이를 처리하는데, lookup은 성능이 떨어지니 조인은 관계형 데이터베이스를 쓰도록 하자

![image](https://user-images.githubusercontent.com/72758925/233775225-4230d223-31d7-45f2-bc2c-2d9b3a086f6d.png)

### 1. 내부 조인

내부 조인은 두 테이블 간에 교집합을 나타낸다.

```sql
SELECT * FROM TableA A 
INNER JOIN TableB B ON 
A.key = B.key
```

### 2. 왼쪽 조인

왼쪽 조인은 테이블 B의 일치하는 부분의 레코드와 함께 테이블 A를 기준으로 완전한 레코드 집합을 생성한다. 만약 테이블 B에 일치하는 항목이 없으면 해당 값은 null 값이 된다.

```sql
SELECT * FROM TableA A 
LEFT JOIN TableB B ON 
A.key = B.key
```

### 3. 오른쪽 조인

오른쪽 조인은 테이블 A에서 일치하는 부분의 레코드와 함께 테이블 B를 기준으로 완전한 레코드 집합을 생성한다. 만약 테이블 A에 일치하는 항목이 없으면 해당 값은 null값이 된다.

```sql
SELECT * FROM TableA A 
RIGHT JOIN TableB B ON 
A.key = B.key
```

### 4. 합집합 조인

합집합 조인(완전 외부 조인)은 양쪽 테이블에서 일치하는 레코드와 함께 테이블 A와 테이블 B의 모든 레코드 집합을 생성한다. 이때 일치하는 항목이 없으면 누락된 쪽에 null값이 포함되어 출력된다.

```sql
SELECT * FROM TableA A 
FULL OUTER JOIN TableB B ON 
A.key = B.key
```