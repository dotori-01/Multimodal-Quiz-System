from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Literal
from DataBase.firebase import db
from datetime import datetime

router = APIRouter()

class AnswerItem(BaseModel):
    quiz_id: str
    user_answer: Literal[0, 1]  # 0: X, 1: O

@router.post("/checkAnswer")
async def check_answers(data: List[AnswerItem]):
    results = []

    for item in data:
        doc = db.collection("quizzes").document(item.quiz_id).get()
        if not doc.exists:
            results.append({
                "quiz_id": item.quiz_id,
                "error": "해당 quiz_id의 문제를 찾을 수 없습니다."
            })
            continue

        quiz = doc.to_dict()
        correct = quiz.get("answer")
        question = quiz.get("question")

        user_answer = "O" if item.user_answer == 1 else "X"
        is_correct = (correct == user_answer)

        db.collection("quiz_results").document().set({
            "quiz_id": item.quiz_id,
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct,
            "is_correct": is_correct,
            "timestamp": datetime.utcnow().isoformat()
        })

        results.append({
            "quiz_id": item.quiz_id,
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct,
            "is_correct": is_correct
        })

    return results
