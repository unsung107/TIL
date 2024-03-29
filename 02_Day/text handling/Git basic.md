## Git ()

### 기본명령어

1. Git 저장소 설정

   ```
   $ git init
   ```

   반드시 현재 디렉토리에 git을 사용하고 있는지, (master) 표기가 없는지 확인할것

   

1.  Git add

   `git add`는 현재 working directory에서 commit 할 목록에 파일들을 담아 놓는 것이다.

   그리고 그 목록은 'index(staging area)' 라고한다.

   ```
   $ git add <폴더이름 혹은 파일이름>
   ```

3. Git commit 

   현재 소스코드 상태를 저장하는것, **스냅샷**을 찍는것과 동일하다.

   'Staging area'(git add로 추가한 파일들이 담기는곳)에 있는 내용을 이력으로 기록한다.

   ```
   $ git commit -m "커밋메시지"
   ```

   

4. Git status

   Git의 현재상태를 확인한다.

   커밋할 목록에 담겨있는지 혹은 untracked 인지., 커밋할 내용이 있는지 등등 다양한 정보를 제공한다.

   ```
   $ git status
   ```

5. Git log

   현재까지 커밋된 모든 이력을 확인 할 수 있다.

   ```
   $ git log
   ```

   

   ## 원격저장소 활용하기

   1. 원격저장소 (remote repository) 등록하기

   ```
   $ git remote add origin _경로_
   ```

   원격 저장소를 등록한다. origin 이라는 이름으로!

   최초에 한번만 등록하면 된다.

   아래의 명령어로 현재 등록된 원격 저장소를 확인 할 수 있다.

   ```
   $git remote -v
   ```

   2. 원격 저장소에 올리기

   ```
   $git push origin master
   ```

   origin 이라는 원격 저장소의 마스터 브랜치로 지금까지의 커밋 내용을 올려줘!

   (브랜치 : 사용용도, 기능 등에 따라 나눠서 저장이 가능한 대분류같은것)

   

   3. 원격저장소에서 가져오기

   ```
   $ git full origin master 
   ```

   4. 원격저장소를 로컬에 복사하기

   ```
   $ git clone __경로__
   ```

   다운받기를 원하는 폴더에서 git bash를 열고 위의 명령어를 입력한다.

   경로는 github에서 우측에 있는 초록색 버튼을 누르면 나타난다.

   

ref : https://backlog.com/git-tutorial/kr/