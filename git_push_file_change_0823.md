## git push 한 데이터 폴더이름 변경하기
=> 변경하고자 하는 상위폴더(.git) 있는 곳으로 옮기기
```git mv oldname newname ```
=> 폴더명 변경

``` git status ```
=> rename 확인
![git_rename](img/git_rename.png)




```git commit -m 'rename'```
=> 변경된 메시지 기록하기
![git_commit](img/git_commit.png)

``` git push origin main ```
=> 다시 git 올리기
![git_push](img/git_push.png)

=> 전처리 데이터 폴더명을 ERD_table로 잘못 저장한 후 git에 올려서 폴더명을 data_preprocessing로 변경한 작업

* 추가적으로 ERD_table 폴더 다시 만들어서 mysql에 Datawarehouse 구축을 위한 자료 push함

8/29 ```git my oldname newname ``` -> 오타수정 my-> mv

8/30  ``` 이미지가 꺠짐``` -> 이미지 경로가 local로 되어 있어서 이미지파일도 같이 git hub에 올려주기