from fastapi import APIRouter, HTTPException
from DataBase.firebase import db

router = APIRouter()

def get_quiz_by_id(quiz_id: str):
    doc = db.collection("quizzes").document(quiz_id).get()
    if doc.exists:
        return doc.to_dict()
    return None

@router.get("/quiz/{quiz_id}")
async def get_quiz(quiz_id: str):
    quiz = get_quiz_by_id(quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="퀴즈를 찾을 수 없습니다.")
    return quiz