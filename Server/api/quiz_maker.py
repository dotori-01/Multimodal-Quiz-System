from fastapi import APIRouter, UploadFile, File #Fast API
from vlm_myopenai.GptVision import analyze_image_with_openai # VLM 연동 완료
from myopenai.ChatTest import generate_quiz, parse_quiz_response # GPT API

router = APIRouter()

@router.post("/uploadImage")
async def upload_image(file: UploadFile = File(...)):
    keywords = analyze_image_with_openai(file) # user 파일 입력
    # print("GPT-4o 응답: ", keywords) # GPT-4o keywords 테스트
    content = generate_quiz(keywords)
    quiz_list = parse_quiz_response(content)
    # print("quiz 배열출력 확인: ",quiz_list)
    return{ "quiz": quiz_list } # 퀴즈 배열 반환
