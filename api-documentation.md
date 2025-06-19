# 📝api 명세서

## 1. server port 번호
8080
## 2. 주소(Home)
http://localhost:8080/

## 3. 이미지 업로드 및 퀴즈 생성
### URL
```http
/api/uploadImage
```
### Method
> POST
### 설명
> 이미지를 업로드하고 키워드 및 퀴즈를 생성한다.<br>
> 이미지 업로드 -> VLM 키워드 추출 -> LLM 퀴즈 생성
### 요쳥 해더
> Content-Type: multipart/form-data
### 요청 파일 형식
> file: UploadFile (jpg/png)
#### 업로드 이미지
![테스트 이미지](test/image/image-1.png)
#### 결과
``` json
{
    "quiz": [
        {
            "quiz_id": "gTJeOGmqU1FwcCRnJNyC",
            "question": "1. 순차적 의사결정은 한 번의 선택이 이후의 선택에 영향을 미치지 않는 독립적인 의사결정 방식이다."
        },
        {
            "quiz_id": "K53cXd4IMwK68ay3PWh7",
            "question": "2. 최적 정책은 주어진 상황에서 가능한 가장 좋은 선택을 결정하는 원칙이다."
        },
        {
            "quiz_id": "KHERz4gU7GKV1nE8U4Gw",
            "question": "3. 확률적 상태 전이는 다음 상태가 현재 상태와 완전히 독립적으로 결정되는 것을 의미한다."
        }
    ]
}
```
### 응답 형식(성공)
> 200 OK

![결과1](test/image/image2.png)

## 4. 퀴즈 내용 DB 저장후 결과
### URL
```http
/api/checkAnswer
```
### Method
> POST
### 설명
> DB(FireBase)에 퀴즈를 저장하고 해당 퀴즈 결과를 리턴
### 요청 해더
> Content-Type: application/json
### 요청 파일 형식
#### 업로드 json 형식
```json
{
  "quiz_id": "gTJeOGmqU1FwcCRnJNyC",
  "user_answer": 1
}
```
#### 결과
```json
{
    "quiz_id": "gTJeOGmqU1FwcCRnJNyC",
    "question": "1. 순차적 의사결정은 한 번의 선택이 이후의 선택에 영향을 미치지 않는 독립적인 의사결정 방식이다.",
    "user_answer": "O",
    "correct_answer": "X",
    "is_correct": false
}
```
### 응답 성공
> 200 OK

![결과2](test/image/image2.png)

### DB 저장
![firebase](test/image/image-2.png)

## 5. 퀴즈 id로 찾기
### URL
```http
/api/quiz/{quiz_id}
```
### Method
> GET
### 설명
> DB(FireBase)에 저장된 퀴즈를 id로 찾아서 가져옴
### 요청 해더
> Content-Type: application/json
### 요청 파일 형식
```http
http://localhost:8080/api/quiz/KHERz4gU7GKV1nE8U4Gw
```
#### 업로드 json 형식
```json
{
    "created_at": "2025-06-16T18:21:29.416914",
    "quiz_id": "KHERz4gU7GKV1nE8U4Gw",
    "question": "3. 확률적 상태 전이는 다음 상태가 현재 상태와 완전히 독립적으로 결정되는 것을 의미한다.",
    "answer": "X"
}
```