### Hadoop

- 다수의 pc를 활용해 빅데이터를 다룬다.

- **분산 저장**

  - 분산 저장의 장점은 클러스터에 컴퓨터를 더하기만 하면 그 컴퓨터의 하드 드라이브가 데이터 저장소의 일부가 된다.
  - Haddop은 클러스터의 모든 하드 드라이브에 걸쳐 분산돼 있는 모든 데이터를  단일 파일 시스템으로 보여준다.
  - 데이터의 여분도 제공
  - 클러스터의 컴퓨터 중 하나에 데이터가 없어져도 데이터으 ㅣ백업 복사본을 클러스터의 다른 컴퓨터에 보관하기에 문제 없다.
  - 이런 상황이 생기면 자동으로 소실된 데이터를 복구하기 때문에 데이터가 회복력이 있어 신뢰 할 수 있다.

- **분산 처리**

  - 데이터를 클러스터 전체에 걸쳐 저장할 뿐만 아니라 그 데이터를 처리할 때도 클러스터의 컴퓨터와 함께한다.

  - 다시 말해, 데이터를 다른 양식으로 전환하거나 다른 시스템으로 전송할 때 혹은 집계해야 할 때

    Hadoop은 이 모든 작업을 병렬로 처리하도록 합니다.

  - 클러스터 내 모든 컴퓨터 CPU에게 이 작업을 분배하여 동시에 처리하게 하는 거죠

  - 이렇게 하면 그 많은 데이터를 신속히 감당할 수 있습니다

- #### 그래서 Hadoop의 장점

  - 빅데이터를 다룰 때 Oracle 데이터베이스에 CPU와 RAID(복수배열 독립 디스크) 추가에 한계
  - 디스크 검색 시간이 더 빠르다.
  - 데이터 손실 위험이 적다.






**HDFS**

- 폴더를 만든다-> name node에게 새 디렉토리 만들겠다고 name node가 응답한것
- 그 폴더에 데이터 파일을 업로드 한다 -> name node에게 파일을 만들어야 하니 위치를 정해달라고 물어본 것