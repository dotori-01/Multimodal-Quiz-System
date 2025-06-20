# Multimodal-Quiz-System
멀티모달 퀴즈 생성 시스템 - VLM과 LLM을 활용한 이미지+텍스트 기반 퀴즈 자동 생성 AI 시스템

# 멀티모달 퀴즈 생성 시스템

## 목차
- [1. 프로젝트 소개](#1-프로젝트-소개)
- [2. 핵심 기능](#2-핵심-기능)
- [3. 아키텍처 다이어그램](#3-아키텍처-다이어그램)
- [4. 기술 스택](#4-기술-스택)
- [5. 웹 실행 방법](#5-웹-실행-방법)
   - [5.1 Server 폴더](#51-server-폴더)
   - [5.2 Multi-modal 폴더](#52-Multi-modal-폴더)
- [6. 사용자 가이드](#6-사용자-가이드)
- [7. 팀원 및 역할 분담](#7-팀원-및-역할-분담)


## 1. 프로젝트 소개
    이미지와 텍스트를 입력받아 AI가 자동으로 퀴즈를 생성하는 멀티모달 시스템입니다.
    VLM(Vision Language Model)이 이미지를 분석하여 키워드를 추출하고, 
    LLM(Large Language Model)이 이를 바탕으로 다양한 형태의 퀴즈를 자동 생성합니다.

## 2. 핵심 기능
- 🖼️ **이미지 분석**: GPT-4o를 활용한 정확한 키워드 추출
- 🧠 **퀴즈 생성**: 맥락을 고려한 OX 퀴즈 자동 생성
- 📊 **실시간 피드백**: 즉석 정답 확인 및 학습
- 🎯 **정답 확인**: 문제 정답 .txt 파일로 제공

## 3. 아키텍처 다이어그램

![image](https://github.com/user-attachments/assets/ac70505a-43c4-43bc-bb56-828d324cbd7a)


## 4. 기술 스택
- **Frontend**: Streamlit
- **Backend**: Flask/FastAPI
- **Database**: Firebase (LLM을 통해 나온 내용을 실시간으로 FireBase에 저장)
- **AI Models**: 
  - VLM: GPT-4o (이미지를 분석하여 키워드 추출)
  - LLM: GPT-4 (분석한 키워드 주제로 0/X 퀴즈 생성)
 
## 5. 웹 실행 방법
### 5.1 Server 폴더
#### 1) 개발 환경 설정
- 명령 프롬프트(cmd) 이용, 아래 명령어로 실행

      .\venv\Scripts\activate

![image](https://github.com/user-attachments/assets/a75a9683-09b6-4e7f-84c2-cb928cf95444)

#### 2) 의존성 패키지 설치
      pip install -r requirements.txt
      
![image](https://github.com/user-attachments/assets/09eb770b-057d-4d61-9857-ce3cab11e039)

#### 3) 서버 실행
      uvicorn main:app --reload --port 8080
      
![image](https://github.com/user-attachments/assets/15fa2293-7627-45cf-9bfb-d9e64eb613e3)


- 자세한 Server-deployment-guide 


(https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/Server/deployment-guide.md) 를 참고하세요.

### 5.2 Multi-modal 폴더

#### 1) phython 설치 
- python 버전 3.8 이상이 설치되어 있어야 한다
* 만약 설치되어 있지 않다면 [Python 공식 홈페이지](https://www.python.org/downloads/)에서 다운로드 후 설치한다

#### 2) 가상환경 설정
      python -m venv venv
      venv\Scripts\activate
      
![image](https://github.com/user-attachments/assets/f067b9aa-29c9-4b97-8c4b-bc3d853fad8e)

#### 3) 의존성 패키지 설치
      pip install -r requirements.txt
      
![image](https://github.com/user-attachments/assets/f466783d-bdc4-4200-9ceb-300b1bfa6396)

#### 4) Streamlit 실행
      streamlit run app.py
  
![image](https://github.com/user-attachments/assets/e2f4261e-b83f-404e-bb67-c0d896314ae6)

- 웹 브라우저 자동 연결
  
![image](https://github.com/user-attachments/assets/85fd76f9-3950-4646-b1b3-b413266d888b)

- 자세한 multi-modal-deployment-guide


https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/multi-modal/deployment-guide.md 를 참고하세요.

 ## 6. 사용자 가이드
### 1) 메인 화면에서 Browse files를 클릭합니다.
   
![image](https://github.com/user-attachments/assets/094de4ff-1fd6-4389-970c-c2c2e1dd65e1)


### 2) 퀴즈 생성 하고싶은 이미지를 선택해 업로드합니다.

![image](https://github.com/user-attachments/assets/0172369a-fdc3-45ef-8080-b711da9cae78)


### 3) 이미지가 업로드되면 자동 퀴즈 생성됩니다.
   
![image](https://github.com/user-attachments/assets/d5c69fe6-89f2-4542-b92a-313f3c18b5ee)




### + + 추가기능
#### 1) 전체 정답 제출 및 결과확인
   
![4](https://github.com/user-attachments/assets/9ce7ba60-c55f-4936-a73b-020cf53027e2)


#### 2) 정답 결과 다운로드 (.txt)

   
![5](https://github.com/user-attachments/assets/9ce4d59f-4a84-4a68-8009-dcd7afda4c0f)

   
![6](https://github.com/user-attachments/assets/bd6135fc-1fbe-4d25-aff5-3185e3bfc273)




- 프로젝트의 자세한 사용법


[(https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/multi-modal/user-guide.md)](https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/multi-modal/user-guide.md) 를 참고하세요.

## 7. 팀원 및 역할 분담
| 역할 | 담당자 | 주요 업무 | 진행 상황 |
|------|--------|-----------|----------|
| 🎯 프로젝트 총괄 | 20210015 도현명 | 전체 일정 관리, GitHub 구조화, 발표 자료 제작 | 진행중 |
| 💻 프론트엔드 | 20210640 고석주 | Streamlit 웹 인터페이스 구현 (Multi-modal 파일) | ✅ 완료 |
| ⚙️ 백엔드 | 20210104 손세영 | API 서버 구축, Firebase 연동 (Server 파일) | ✅ 완료 |
| 👁️ VLM 연동 | 20200852 오예찬 | 이미지 분석 모듈 개발 | ✅ 완료 |
| 🧠 LLM 연동 | 20231386 성원제 | 퀴즈 생성 모듈 개발 | ✅ 완료 |
| 🔍 QA/테스트 & 시연 영상 담당 | 20210428 장지원 | 품질 보증 및 시연 영상 준비 | ⏳ 대기중 |



