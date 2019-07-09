# Git (수정되었습니다)))

(분산) 버전관리 시스템

코드의 히스토리를 관리하는 도구.개발된 과정과 역사를 볼수 ㅣㅇ쓰며 프로젝트의 이전 버젼을 복원하고 변경사항을 비교 분석 및 병합도 가능

### DVCS

distributed version control system

### git의 작업흐름

add : 커밋할 목록에 추가

commit : 커밋 만들기

push 현재까지의 역사(커밋) 가 기록되어있는곳에 새로 생성한 커밋들 반영하기

### git의 기본

$ git add helloworld.py 커밋할 목록에 담아둠 argument 한개

$ git commit -m 메시지를 남기겠습니다 메시지는 필수기능 

$ git config --global user.name "John"

### git 초기화(2~3중 택1)

1. git bash 실행 후 미리 설정되어있을지 모를 계정정보 삭제

$git config --global --unset credential.helper

$git config --system --unset credential.helper



2. 윈도우 자격 증명 관리자에서 git 관련 정보삭제
3.  git bash 실행 후 아래와 같이 입력

$git credential reject

protocal=https

host=github.com

----

git config --global user.name & email ""

git init (내가 사용할 폴더)

마스터 표시가 없을때 git init

git init을 한상태에서 다른 디렉토리에서 init하면 저장소가 또 생기는것

---

git add , git commit -m " " , git status , git log

git remote  = 원격저장소 관리 키워드

git remote origin https://github.com/unsung107/TIL.git



origin 이라는 이름으로 remote를 등록하겠다(리모트의 이름)

git push origin master

git full origin master = 깃허브에 올라온 새로운 커밋을 가져옴

git hub - clone or download 여기서 주소복사

후 
