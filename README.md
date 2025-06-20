# Multimodal-Quiz-System
멀티모달 퀴즈 생성 시스템 - VLM과 LLM을 활용한 이미지+텍스트 기반 퀴즈 자동 생성 AI 시스템

# 멀티모달 퀴즈 생성 시스템

## 목차
1. [프로젝트 소개](#1.-프로젝트-소개)
2. [주요 기능](#주요-기능)
3. [아키텍처 다이어그램](#아키텍처-다이어그램)
4. [기술 스택](#기술-스택)
5. [실행 방법 및 사용자 가이드](#실행-방법-및-사용자-가이드)
6. [프로젝트 파일 구조](#프로젝트-파일-구조)
7. [팀원 및 역할 분담](#7.-팀원-및-역할-분담)


## 1. 프로젝트 소개
    이미지와 텍스트를 입력받아 AI가 자동으로 퀴즈를 생성하는 멀티모달 시스템이다.
    VLM(Vision Language Model)이 이미지를 분석하여 키워드를 추출하고, 
    LLM(Large Language Model)이 이를 바탕으로 다양한 형태의 퀴즈를 자동 생성한다.

## 2. 주요 기능
    - 🖼️ **이미지 분석**: GPT-4o를 활용한 정확한 키워드 추출
    - 🧠 **퀴즈 생성**: 맥락을 고려한 다양한 유형의 퀴즈 자동 생성
    - 📊 **실시간 피드백**: 즉석 정답 확인 및 학습 효과 분석
    - 🎯 **다양한 형태**: 객관식, 주관식, 서술형 퀴즈 지원

## 3. 아키텍처 다이어그램

![image](https://github.com/user-attachments/assets/ac70505a-43c4-43bc-bb56-828d324cbd7a)


## 4. 기술 스택
- **Frontend**: Streamlit
- **Backend**: Flask/FastAPI
- **Database**: Firebase
- **AI Models**: 
  - VLM: GPT-4o (이미지 분석)
  - LLM: GPT API (퀴즈 생성)
 
## 5. 실행 방법
### 5.1 Server 폴더
#### 1) 환경설정 활성화

![image](https://github.com/user-attachments/assets/a75a9683-09b6-4e7f-84c2-cb928cf95444)

#### 2) 의존성 패키지 설치

![image](https://github.com/user-attachments/assets/09eb770b-057d-4d61-9857-ce3cab11e039)

#### 3) 서버 연결

![image](https://github.com/user-attachments/assets/15fa2293-7627-45cf-9bfb-d9e64eb613e3)

### 5.2 Multi-modal 폴더

#### 1) phython 설치 
- python 버전 3.8 이상이 설치되어 있어야 한다
* 만약 설치되어 있지 않다면 [Python 공식 홈페이지](https://www.python.org/downloads/)에서 다운로드 후 설치한다

#### 2) 가상환경 설정
- 아래 명령어로 가상환경 설정

      python -m venv venv
      venv\Scripts\activate
![image](https://github.com/user-attachments/assets/f067b9aa-29c9-4b97-8c4b-bc3d853fad8e)

#### 3) 의존성 패키지 설치
- 아래 명령어로 필요한 패키지를 설치
  
      pip install -r requirements.txt
![image](https://github.com/user-attachments/assets/f466783d-bdc4-4200-9ceb-300b1bfa6396)

#### 4) Streamlit 실행 및 웹 브라우저 자동 연결
- 아래 명령어로 Streamlit 실행

      streamlit run app.py 
![image](https://github.com/user-attachments/assets/e2f4261e-b83f-404e-bb67-c0d896314ae6)

![image](https://github.com/user-attachments/assets/2ed929c9-8dce-48d0-9f9b-63975b815c18)


## 6. 프로젝트 파일 구조


## 7. 팀원 및 역할 분담
| 역할 | 담당자 | 주요 업무 | 진행 상황 |
|------|--------|-----------|----------|
| 🎯 프로젝트 관리/발표 | 20210015 도현명 | 전체 일정 관리, GitHub 구조화, 발표 자료 제작 | 진행중 |
| 💻 프론트엔드 | 20210640 고석주 | Streamlit 웹 인터페이스 구현 | ✅ 완료 |
| ⚙️ 백엔드 | 20210104 손세영 | API 서버 구축, Firebase 연동 | ✅ 완료 |
| 👁️ VLM 연동 | 20200852 오예찬 | 이미지 분석 모듈 개발 | ✅ 완료 |
| 🧠 LLM 연동 | 20231386 성원제 | 퀴즈 생성 모듈 개발 | ✅ 완료 |
| 🔍 QA/테스트 | 20210428 장지원 | 품질 보증 및 시연 준비 | ⏳ 대기중 |



