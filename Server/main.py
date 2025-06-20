import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.quiz_maker import router as image_upload_router
from api.answer_checker import router as answer_checker
from api.answer_get import router as answer_get

app = FastAPI()
app.include_router(image_upload_router, prefix="/api")
app.include_router(answer_checker, prefix="/api")
app.include_router(answer_get, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 프론트 주소
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def Server_status():
    return {"status": "OK", "message": "Server is running"}

if __name__ == "__main__":
    app.uvicorn("main:app", port=8080, reload=True)

# 로컬 실행용: uvicorn main:app --reload --port 8080