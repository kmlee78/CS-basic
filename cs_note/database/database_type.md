[1. 관계형 데이터베이스](#1-관계형-데이터베이스)\
[2. NoSQL 데이터베이스](#2-nosql-데이터베이스)

## 1. 관계형 데이터베이스

> 관계형 데이터베이스(RDBMS)는 행과 열을 가지는 표 형식 데이터를 저장하는 형태의 데이터베이스를 가리키며 SQL이라는 언어를 써서 조작한다.
> 

### MySQL

대부분의 운영체제와 호환되며 현재 가장 많이 사용하는 데이터베이스.

MylSAM 인덱스 압축 기술, B-트리 기반의 인덱스, 스레드 기반의 메모리 할당 시스템, 매우 빠른 조인, 최대 64개의 인덱스를 제공한다. 대용량 데이터베이스를 위해 설계되어 있고 롤백, 커밋, 이중 암호 지원 보안 등의 기능을 제공.

### PostgreSQL

디스크 조각이 차지하는 영역을 회수할 수 있는 장치인 VACUUM이 특징. 최대 테이블의 크기는 32TB이며 SQL뿐만 아니라 JSON을 이용해서 데이터에 접근할 수 있다. 지정 시간에 복구하는 기능, 로깅, 접근 제어, 중첩된 트랜잭션, 백업 등을 할 수 있다.

---

## 2. NoSQL 데이터베이스

> SQL을 사용하지 않는 데이터베이스를 말하며, 대표적으로 MongoDB와 redis 등이 있다.
> 

### MongoDB

JSON을 통해 데이터에 접근할 수 있고, Binary JSON 형태(BSON)로 데이터가 저장되며 와이어드타이거 엔진이 기본 스토리지 엔진으로 장착된 키-값 데이터 모델에서 확장된 도큐먼트 기반의 데이터베이스.

확장성이 뛰어나며 빅데이터를 저장할 때 성능이 좋고 고가용성과 샤딩, 레플리카셋을 지원한다.

또한, 도큐먼트를 생성할 때마다 다른 컬렉션에서 중복된 값을 지니기 힘든 유니크한 값인 ObjectID가 생성됨

### redis

인메모리 데이터베이스이자 키-값 데이터 모델 기반의 데이터베이스. 기본적인 데이터 타입은 문자열(string)이며 최대 512MB까지 저장할수 있다.

pub/sub 기능을 통해 채팅 시스템, 다른 데이터베이스 앞단에 두어 사용하는 캐싱 계층, 단순한 키-값이 필요한 세션 정보 관리, 정렬된 셋(sorted set) 자료 구조를 이용한 실시간 순위표 서비스에 사용한다.