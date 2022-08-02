# GIT

폴더만들기

`git init` : git 시작

* 계정 연결
  * `git config --local user.username '<gitlab username>'`(파일안 계정연결,
  * `전체 연결하려면 local -> global`
  * `git config --local user.email'<gitlab email>'` 
* project / repository  연결
  * `git remote add origin <gitlab url>`

`git status` : 상태 확인

`git add .` : 모든 파일 다 올려줘

`git add <file_name>`: 특정 파일만 올려줘

`git commit -m '<commit message>'`  메시지 작성

`git push origin master`

`git pull origin master` : gitlab/ github에 있는거 가져와

- 푸쉬가 안될경우 
  
  1. git pull origin master --allow-unrelated-histories 해보기
     
     1