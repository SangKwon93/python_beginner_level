## Ec2 상 mongoDB 셋팅
# .ssh 폴더에 들어간다.
``` ssh -i "skp.pem" ubuntu@ec2-54-180-117-81.ap-northeast-2.compute.amazonaws.com ``` 을 통해서 연결

# 업데이트
```sudo apt update -y ``` -y는 중간중간 질문에 yes 작성 자동
``` sudo apt upgrade -y  ```

# mongodb 설치
``` sudo apt install -y mongodb ```

# mongodb 작동중인지 확인
``` sudo systemctl status mongodb ```

# mongodb 설정파일 수정
``` sudo vi /etc/mongodb.conf ```
=> bind_ip를 0.0.0.0으로 변경(어디에서나 접속가능)

# 파일 수정되어서 재시작
``` sudo systemctl restart mongodb```

# mongodb 접속하려면 명령어
``` mongo ``` 

# 데이터베이스 확인
show databases

# databases 생성
use database명

=> db.collection명.insert(json형식으로 (dict)) 작성하면 collection명 생김

# collections 확인
show collections

# collections 안에 데이터 확인하기
db.collection.find().pretty()

# collection 삭제하기
db.collection.drop()

## scrpay pipeline.py mongodb 연동 시 

``` client = pymongo.MongoClient('mongodb://localhost:27017/') ```
``` db = client.resell ``` 


