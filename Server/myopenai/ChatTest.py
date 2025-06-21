import os, re
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
from DataBase.firebase import db

load_dotenv("./myopenai/apikey.env")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")

client = OpenAI(api_key=api_key)

def generate_quiz(keywords: str) -> str: 
    prompt = (
        "다음 키워드를 기반으로 OX 퀴즈 3개를 만들어줘.\n"
        "- 각 퀴즈는 하나의 문장이어야 하고, 문장 끝에 반드시 (O) 또는 (X) 형식으로 정답을 써줘.\n"
        "- 숫자나 기호 없이 문장만 작성하고, 줄마다 하나씩 출력해줘.\n\n"
        f"키워드: {keywords}"
    )
    return chat_with_gpt(prompt)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("GPT 응답이 없습니다. LLM 요청을 확인해주세요.")
    return content

def parse_quiz_response(response: str) -> list[dict]:
    lines = response.strip().split("\n")
    quiz_list = []

    for line in lines:
        match = re.match(r"(.+?)\s*\((O|X)\)\s*$", line.strip())
        if match:
            question = match.group(1).strip()
            answer = match.group(2).strip().upper()

            quiz_id = save_quiz_to_firestore(question, answer)

            quiz_list.append({
                "quiz_id": quiz_id,
                "question": question
            })
    
    return quiz_list

def save_quiz_to_firestore(question: str, answer: str) -> str:
    doc_ref = db.collection("quizzes").document()
    quiz_id = doc_ref.id
    doc_ref.set({
        "quiz_id": quiz_id,
        "question": question,
        "answer": answer,
        "created_at": datetime.utcnow().isoformat()
    })
    return quiz_id