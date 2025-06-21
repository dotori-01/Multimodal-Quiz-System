import base64, os

from dotenv import load_dotenv
from openai import OpenAI
from fastapi import UploadFile

load_dotenv("./vlm_myopenai/apikey.env")
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def encode_image_base64(file: UploadFile) -> str:
    file.file.seek(0)
    image_bytes = file.file.read()
    return base64.b64encode(image_bytes).decode("utf-8")

def analyze_image_with_openai(file: UploadFile) -> str:
    
    encoded_image = encode_image_base64(file) # base64 인코딩
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        { "type": "text", "text": "이 이미지를 보고 키워드 3개를 만들어줘" },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=100
        )
        content = response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"GPT 호출 실패: {str(e)}")
    
    if content is None:
        raise ValueError("GPT 응답이 없습니다. VLM 요청을 확인해주세요.")
    return content