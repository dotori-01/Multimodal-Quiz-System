# 🤖 멀티모달 퀴즈 생성 시스템
 VLM과 LLM을 활용한 이미지+텍스트 기반 퀴즈 자동 생성 AI 시스템

## 목차
- [1. 프로젝트 소개](#1-프로젝트-소개)
- [2. 핵심 기능](#2-핵심-기능)
- [3. 아키텍처 다이어그램](#3-아키텍처-다이어그램)
- [4. 기술 스택](#4-기술-스택)
- [5. 프로젝트 파일 구조](#5-프로젝트-파일-구조)
- [6. 웹 실행 방법](#6-웹-실행-방법)
   - [6.1 Server 폴더](#61-server-폴더)
   - [6.2 Multi-modal 폴더](#62-Multi-modal-폴더)
- [7. 사용자 가이드](#7-사용자-가이드)
- [8. api 명세서](#8-api-명세서)
- [9. 팀원 및 역할 분담 (팀 5)](#9-팀원-및-역할-분담-팀-5)

- - -
## 1. 프로젝트 소개
### 소프트웨어공학 팀 프로젝트 과제 [팀 5]
    이미지와 텍스트를 입력받아 AI가 자동으로 퀴즈를 생성하는 멀티모달 시스템입니다.
    VLM(Vision Language Model)이 이미지를 분석하여 키워드를 추출하고, 
    LLM(Large Language Model)이 이를 바탕으로 다양한 형태의 퀴즈를 자동 생성합니다.
    
- - -

## 2. 핵심 기능
- 🖼️ **이미지 분석**: GPT-4o를 활용한 정확한 키워드 추출
- 💬 **퀴즈 생성**: 맥락을 고려한 OX 퀴즈 자동 생성
- 📊 **실시간 피드백**: 즉석 정답 확인 및 학습
- ✅ **정답 확인**: 문제 정답 .txt 파일로 제공
  
- - -

## 3. 아키텍처 다이어그램

![Gpt_Quiz drawio](https://github.com/user-attachments/assets/7f3b209f-f058-46a0-a429-b0830d5dbc90)

- - -

## 4. 기술 스택
| 🛠️ 분야       | 기술 및 설명                                                                 |
|--------------|-----------------------------------------------------------------------------|
| 🌐 Frontend  | Streamlit                                                                   |
| 🖥️ Backend   | Flask / FastAPI                                                             |
| 🗄️ Database  | Firebase (LLM을 통해 나온 내용을 실시간으로 FireBase에 저장)               |
| 🤖 AI Models | VLM: GPT-4o (이미지를 분석하여 키워드 추출)                                |
|              | LLM: GPT-4 (분석한 키워드 주제로 0/X 퀴즈 생성)                            |

- - -

 ## 5. 프로젝트 파일 구조
 
      multimodal-quiz-system/
      ├── 📂 backend/                  # 백엔드 서버 (Server 폴더)
      │   ├── 📂 __pycache__/          # 파이썬 캐시 파일
      │   ├── 📂 api/                  # API 엔드포인트 모듈
      │   ├── 📂 DataBase/             # 데이터베이스 관련 파일
      │   ├── 📂 myopenai/             # OpenAI 연동 모듈
      │   ├── 📂 test/                 # 테스트 코드
      │   ├── 📂 venv/                 # 가상환경(커밋 제외)
      │   ├── 📂 vlm_myopenai/         # VLM(OpenAI) 연동 모듈
      │   ├── 📄 .gitignore            # Git 무시 파일 목록
      │   ├── 📄 api-documentation     # API 명세서 (Markdown)
      │   ├── 📄 deployment-guide      # 배포 가이드 (Markdown)
      │   ├── 📄 main                  # 서버 실행 파일 (Python)
      │   └── 📄 requirements          # 의존성 목록 (requirements.txt)
      │
      ├── 📂 frontend/                 # 프론트엔드 (multi-modal 폴더)
      │   ├── 📂 __pycache__/          # 파이썬 캐시 파일
      │   ├── 📂 assets/               # 정적 자산(CSS 등)
      │   ├── 📂 components/           # UI 컴포넌트
      │   ├── 📂 venv/                 # 가상환경(커밋 제외)
      │   ├── 📄 app                   # 메인 앱 (Python)
      │   ├── 📄 config                # 환경설정 파일
      │   ├── 📄 deployment-guide      # 배포 가이드 (Markdown)
      │   ├── 📄 requirements          # 의존성 목록 (requirements.txt)
      │   └── 📄 user-guide            # 사용자 가이드 (Markdown)

- - -
 
## 6. 웹 실행 방법
### 6.1 Server 폴더
#### 1️⃣  개발 환경 설정
- 명령 프롬프트(cmd) 이용, 아래 명령어로 실행

      .\venv\Scripts\activate

![9 개발환경](https://github.com/user-attachments/assets/5eee471a-c80a-442b-a1fb-3cefa91badca)


#### 2️⃣ 의존성 패키지 설치
      pip install -r requirements.txt
      
![10](https://github.com/user-attachments/assets/3dc068b5-d8e7-484c-93ed-b0af259130ba)


#### 3️⃣ 서버 실행
      uvicorn main:app --reload --port 8080
      
![11 서버실행](https://github.com/user-attachments/assets/32d30629-884b-4b89-9e9c-b2dd5828f41b)



📖 자세한 Server-deployment-guide 


(https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/Server/deployment-guide.md) 를 참고하세요.
- - -
### 6.2 Multi-modal 폴더

#### 1️⃣ phython 설치 
- python 버전 3.8 이상이 설치되어 있어야 한다
* 만약 설치되어 있지 않다면 [Python 공식 홈페이지](https://www.python.org/downloads/)에서 다운로드 후 설치한다

#### 2️⃣ 가상환경 설정
      python -m venv venv
      venv\Scripts\activate
      
![12  가상환경](https://github.com/user-attachments/assets/c7d1b8a3-dbe6-471d-9d08-b2959b7d25df)



#### 3️⃣ 의존성 패키지 설치
      pip install -r requirements.txt
      
![의존성 패키지 13](https://github.com/user-attachments/assets/6739db9c-4422-4def-9d3d-eaf8750fa207)



#### 4️⃣ Streamlit 실행
      streamlit run app.py
  
![15 streamlit](https://github.com/user-attachments/assets/fadf4b33-1946-4bc0-ae35-957173599832)


- 웹 브라우저 자동 연결
  
![image](https://github.com/user-attachments/assets/85fd76f9-3950-4646-b1b3-b413266d888b)

📖 자세한 multi-modal-deployment-guide


https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/multi-modal/deployment-guide.md 를 참고하세요.

- - -

 ## 7. 사용자 가이드
### 1️⃣ 메인 화면에서 Browse files를 클릭합니다.
   
![image](https://github.com/user-attachments/assets/094de4ff-1fd6-4389-970c-c2c2e1dd65e1)


### 2️⃣ 퀴즈 생성 하고싶은 이미지를 선택해 업로드합니다.

![image](https://github.com/user-attachments/assets/5a75dcd2-af32-4c97-a9a0-14832308685c)



### 3️⃣ 이미지가 업로드되면 자동 퀴즈 생성됩니다.
   
![image](https://github.com/user-attachments/assets/f85ca951-b0cb-4fba-b501-4d813937fd44)





### 4️⃣ 전체 정답 제출 및 결과 확인
   
![4](https://github.com/user-attachments/assets/9ce7ba60-c55f-4936-a73b-020cf53027e2)


### 5️⃣ 정답 결과 다운로드 (.txt)

   
![5](https://github.com/user-attachments/assets/9ce4d59f-4a84-4a68-8009-dcd7afda4c0f)

   
![6](https://github.com/user-attachments/assets/bd6135fc-1fbe-4d25-aff5-3185e3bfc273)


📖 프로젝트의 자세한 사용법


[(https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/multi-modal/user-guide.md)](https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/multi-modal/user-guide.md) 를 참고하세요.

- - -

## 8. Api 명세서 
https://github.com/dotori-01/Multimodal-Quiz-System/blob/main/Server/api-documentation.md 를 참고하세요.

- - -

## 9. 팀원 및 역할 분담 (팀 5)
| 역할 | 담당자 | 주요 업무 | 진행 상황 |
|------|--------|-----------|----------|
| 🎯 프로젝트 총괄 | 20210015 도현명 | 전체 일정 관리, GitHub 구조화, 발표 자료 제작 | 진행중 |
| 💻 프론트엔드 | 20210640 고석주 | Streamlit 웹 인터페이스 구현 (Multi-modal 개발) | ✅ 완료 |
| ⚙️ 백엔드 | 20210104 손세영 | API 서버 구축, Firebase 연동 (Server 개발) | ✅ 완료 |
| 👁️ VLM 연동 | 20200852 오예찬 | 이미지 분석 모듈 개발 | ✅ 완료 |
| 🧠 LLM 연동 | 20231386 성원제 | 퀴즈 생성 모듈 개발 | ✅ 완료 |
| 🔍 QA/테스트&시연 영상| 20210428 장지원 | 품질 보증 및 시연 영상 준비 | ⏳ 대기중 |



