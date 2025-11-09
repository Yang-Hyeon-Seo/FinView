# FinView

Django 기반 금융 커뮤니티 서비스 프로젝트
사용자 인증 기능과 게시글 작성·수정·조회가 가능한 게시판을 포함

## 1. 기술 스택

- Python 3.11
- Django 5.2.8
- SQLite3
- 가상환경: venv

## 2. 주요 기능
### 2.1 사용자 인증 (accounts 앱)
- 로그인
- 로그아웃
- 회원가입
- 회원탈퇴
- 회원정보 수정
- 비밀번호 변경

### 2.2 게시글 기능 (posts 앱)
- 게시글 조회
- 게시글 생성
- 게시글 수정
- 게시글 삭제
- 댓글 생성
- 댓글 삭제

## 3. 컨벤션
### 3.1 커밋 메시지
- 기능 : `feature-01-login`
- 수정 : `fix-01-login`
- 참고 : [참고블로그](https://sungwookoo.tistory.com/1)

### 3.2 브랜치명
- 기능 : `feature/login` 이런식으로 이름 정하기

## 4. 브랜치 용도
- master: 최종 프로젝트
- develop: 개발 중 병합 브랜치
- fearure/user-model: F02 - 모델 상속
- feature/form-custom: F03 - 기본 폼 CUSTOM
- feature/login: F07 - 로그인
- feature/logout: F08 - 로그아웃
- fearure/signup: F09 - 회원가입
- feature/delete: F11 - 회원탈퇴
- feature/index: F13 - 금융 게시글 조회
- feature/detail: F15 - 게시글 상세 조회
- fearure/update: F16 - 게시글 수정
- fix/authenticated: 인증된 사용자에 의한 접근 제한
- feature/10-update : F10 - 회원 정보 수정
- feature/12-change_password : F12 - 비밀번호 변경
- feature/14-create : F14 - 게시글 작성
- feature/17-delete : F17 - 게시글 삭제
- feature/18-comment_create : F18 - 댓글 작성
- feature/19-comment_delete : F19 - 댓글 삭제

## 5. 커밋
![commit-4](image4.png)
![commit-3](image3.png)
![commit-2](image2.png)
![commit-1](image1.png)

## 6. 코드 소개
- 비밀번호 수정(현서)
  - 코드 작성 및 수정 과정이 가장 어려웠음
  - `


## 7. 배운점 및 느낀점