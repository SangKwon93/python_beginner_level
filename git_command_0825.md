## git 초기 세팅 및 command
# 계정 설정
``` git config --global user.name "skpark" ```
```git config --global user.email "apfhda7@gmail.com" ```

# window와 mac 형태 맞추기
``` git config --global core.autocrlf true ```
# 운영체제 마다 Editor에서 새로운 줄바꿈을 할 떄 문자열이 달라진다.
Window의 경우 /r (carriage-return) + /n (line feed)
MAC의 경우 /n (line feed)

# core.autocrlf true 설정 시 
git 저장할 떄 /r 삭제
git에서 window상 보낼 때 자동으로 /r 붙여준다.

# github 파일 올리기
mkdir를 활용하여 폴더 생성
폴더 안에 git 폴더를 만든다.
``` ls -al " list 확인" ``` => list 확인
``` git init ``` => ls -al 하면 .git 생성(숨겨진 파일은 . 이 붙는다.) => master branch가 생긴다.
``` rm -rf.git ``` => git 삭제 시 사용
``` git config --global alias.st status ``` => git status 를 짧게 작성하여 활용

``` git rm --cached * ``` =>  staging area에서 working directory untracked로 돌아온다.
``` git status -s ``` => 간단하게 상태 확인
ex) A초록색 stage area에 추가된 정보
    ??. working directory에만 있음
    AM stage area에 추가된 정보에서 수정된 경우

```git diff``` => 이전 버전과 비교하기 => 변경된 부분은 초록색으로 표시

```cat 파일명.확장명 ``` => 터미널 창에 해당파일 내용이 나온다.

```git commit -am '메시지'``` => working stage와 staging area 둘다 커밋됨

```git add *.md``` => .md 확장명 전체 커밋하기