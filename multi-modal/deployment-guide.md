# 멀티모달 퀴즈 생성 시스템  가이드

## 설치 및 실행 방법

### 1. Python 설치
- python 버전 3.8 이상이 설치되어 있어야 한다
* 만약 설치되어 있지 않다면 [Python 공식 홈페이지](https://www.python.org/downloads/)에서 다운로드 후 설치한다

### 2. 프로젝트 폴더 준비
- 예시:  `C:\사용자\사용자이름\프로젝트경로\mulit-modal` 폴더에 프로젝트 파일이 위치해야 한다

### 3. 가상환경(선택 사항)
- 가상환경을 사용하는 것이 좋다 (필수는 아니다)
- 명령 프롬포트(cmd)에서 아래 명령어를 입력
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

### 4. 의존성 패키지 설치
- 아래 명령어로 필요한 패키지를 설치
    ```
    pip install -r requirements.txt
    ```
- `requirements.txt`에 `streamlit`, `requests` 등이 포함되어 있는지 확인

### 5. assets/style.css 파일 확인
- `assets/style.css` 파일이 존재하는지, 원하는 스타일이 작성되어 있는지 확인

### 6. Streamlit 앱 실행
- `app.py`가 있는 파일에서 아래 명령어를 실행해야 함
    ```
    streamlit run app.py
    ```

### 7. 웹 브라우저에 접속
- 명령어가 실행되면 자동으로 브라우저가 열린다
* 만약 브라우저가 열리지 않으면 터미널에 표시된 URL(예: http://localhost:8501)을 복사해 브라우저에 붙여넣으면 된다

### 8. 주요 사용 과정
1. '이미지 업로드' 버튼을 클릭해 이미지를 업로드한다
2. 업로드 후 퀴즈 생성 결과가 화면에 표시된다
3. 만약 스타일이 적용되지 않는다면 브라우저를 새로고침 하면 된다

### 9. 오류 해결
- `ModuleNotFoundError: No module named 'streamlit'`  
  -> `pip install streamlit` 명령어로 streamlit을 설치
- `File does not exist: app.py`  
  -> 터미널에서 `app.py`가 있는 폴더로 이동한 뒤 실행
- 스타일이 적용되지 않을 경우  
  -> `assets/style.css` 파일 경로와 내용 확인

----------
## 환경 변수 및 설정
- `config.py`에서 환경설정(예: 업로드 허용 확장자, 백엔드 서버 주소 등)을 할 수 있다
- 예시:
    ```python
    BACKEND_URL = "http://localhost:8080"
    ```

## 배포 시 유의사항
- 외부 API 연동 시 API 키 등 민감 정보는 별도로 관리해야 한다 (예: .env, gitignore 등)
- 정적 파일(assets/) 경로가 올바른지 확인해야 한다
