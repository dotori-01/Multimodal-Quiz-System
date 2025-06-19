import streamlit as st
import requests
import io
from config import BACKEND_URL

st.set_page_config(page_title = "멀티모달 퀴즈 생성 시스템", layout = "centered")

# 스타일 적용 (현재 적용은 안한 상태)
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
except FileNotFoundError:
    pass

st.title("멀티모달 퀴즈 생성 시스템")
st.write("이력서 이미지를 업로드하면 AI가 자동으로 퀴즈를 생성합니다.")

# 퀴즈 재시도/다시 풀기 기능
if st.button("새 이미지로 다시 시작하기"):
    st.rerun()

uploaded_file = st.file_uploader("이력서 이미지 업로드", type = ["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 예외 처리: 파일 크기 및 확장자 체크
    if uploaded_file.size > 10 * 1024 * 1024:
        st.warning("10MB 이하의 이미지만 업로드할 수 있습니다.")
    elif not uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        st.warning("PNG, JPG, JPEG 파일만 업로드 가능합니다.")
    else:
        st.image(uploaded_file, caption = "업로드한 이력서", use_container_width = True)
        with st.spinner("퀴즈를 생성 중입니다..."):
            try:
                files = {'file': (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(f"{BACKEND_URL}/api/uploadImage", files = files)
                response.raise_for_status()
                data = response.json()
                st.success("퀴즈가 성공적으로 생성되었습니다! 아래 문제를 풀어보세요.")
                for quiz in data["quiz"]:
                    st.markdown(f"**{quiz['question']}**")
                    user_answer = st.radio(
                        f"정답을 선택하세요 (quiz_id: {quiz['quiz_id']})",
                        ("O", "X"),
                        key = quiz["quiz_id"]
                    )
                    if st.button("정답 제출", key = f"submit_{quiz['quiz_id']}"):
                        answer_payload = {
                            "quiz_id": quiz["quiz_id"],
                            "user_answer": 1 if user_answer == "O" else 0
                        }
                        try:
                            answer_response = requests.post(
                                f"{BACKEND_URL}/api/checkAnswer",
                                json = answer_payload,
                                headers = {"Content-Type": "application/json"}
                            )
                            answer_response.raise_for_status()
                            result = answer_response.json()
                            # UX: 정답 여부에 따라 시각적 효과
                            if result["is_correct"]:
                                st.success(f"정답입니다! 🎉 (정답: {result['correct_answer']})")
                            else:
                                st.error(f"오답입니다. 😢 (정답: {result['correct_answer']})")
                            # 결과 다운로드 기능
                            result_text = (
                                f"문제: {result['question']}\n"
                                f"내 답: {result['user_answer']}\n"
                                f"정답: {result['correct_answer']}\n"
                                f"정답 여부: {'정답' if result['is_correct'] else '오답'}"
                            )
                            st.download_button(
                                "결과 다운로드",
                                io.StringIO(result_text),
                                file_name = f"quiz_result_{quiz['quiz_id']}.txt"
                            )
                        except requests.exceptions.RequestException:
                            st.error("정답 제출 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")
            except requests.exceptions.RequestException:
                st.error("서버와 연결할 수 없습니다. 잠시 후 다시 시도해 주세요.")
else:
    st.info("이력서 이미지를 업로드해 주세요.")