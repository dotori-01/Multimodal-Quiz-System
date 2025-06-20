import streamlit as st
import requests
import io
from config import BACKEND_URL

st.set_page_config(page_title="멀티모달 퀴즈 생성 시스템", layout="centered")

try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.title("멀티모달 퀴즈 생성 시스템")
st.write("이미지를 업로드하면 AI가 자동으로 퀴즈를 생성합니다.")

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "submitted_results" not in st.session_state:
    st.session_state.submitted_results = None

if st.button("새 이미지로 다시 시작하기"):
    st.session_state.quiz_data = None
    st.session_state.user_answers = {}
    st.session_state.submitted_results = None
    st.rerun()

uploaded_file = st.file_uploader("이미지 업로드", type=["png", "jpg", "jpeg"])

if uploaded_file:
    if uploaded_file.size > 10 * 1024 * 1024:
        st.warning("10MB 이하의 이미지만 업로드할 수 있습니다.")
    elif not uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        st.warning("PNG, JPG, JPEG 파일만 업로드 가능합니다.")
    elif st.session_state.quiz_data is None:
        st.image(uploaded_file, caption="업로드한 이력서", use_container_width=True)

        with st.spinner("퀴즈를 생성 중입니다..."):
            try:
                files = {'file': (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(f"{BACKEND_URL}/api/uploadImage", files=files)
                response.raise_for_status()
                st.session_state.quiz_data = response.json()
                st.success("퀴즈가 성공적으로 생성되었습니다! 아래 문제를 풀어보세요.")
            except requests.exceptions.RequestException as e:
                st.error("서버와 연결할 수 없습니다.")
                st.write("오류 로그:", e)

if st.session_state.quiz_data:
    data = st.session_state.quiz_data
    st.subheader("OX 퀴즈")

    for quiz in data["quiz"]:
        quiz_id = quiz["quiz_id"]
        question = quiz["question"]
        st.markdown(f"**{question}**")

        answer_key = f"user_answer_{quiz_id}"
        if answer_key not in st.session_state.user_answers:
            st.session_state.user_answers[answer_key] = "O"

        selected = st.radio(
            "정답을 선택하세요",
            ("O", "X"),
            key=answer_key,
            index=0
        )
        st.session_state.user_answers[answer_key] = selected

    if st.button("전체 정답 제출"):
        try:
            answer_payload = [
                {
                    "quiz_id": quiz["quiz_id"],
                    "user_answer": 1 if st.session_state.user_answers[f"user_answer_{quiz['quiz_id']}"] == "O" else 0
                }
                for quiz in data["quiz"]
            ]

            response = requests.post(
                f"{BACKEND_URL}/api/checkAnswer",
                json=answer_payload,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            st.session_state.submitted_results = response.json()

        except requests.exceptions.RequestException as e:
            st.error("정답 제출 중 오류가 발생했습니다.")
            st.write("오류 로그:", e)

if st.session_state.submitted_results:
    st.subheader("정답 결과")
    for result in st.session_state.submitted_results:
        if result.get("error"):
            st.error(f"[{result['quiz_id']}] 오류: {result['error']}")
            continue

        if result["is_correct"]:
            st.success(f"✅ 정답: {result['question']} (정답: {result['correct_answer']})")
        else:
            st.error(f"❌ 오답: {result['question']} (정답: {result['correct_answer']})")

        result_text = (
            f"문제: {result['question']}\n"
            f"내 답: {result['user_answer']}\n"
            f"정답: {result['correct_answer']}\n"
            f"정답 여부: {'정답' if result['is_correct'] else '오답'}"
        )

        st.download_button(
            "결과 다운로드",
            data=result_text,
            file_name=f"quiz_result_{result['quiz_id']}.txt",
            mime="text/plain"
        )
else:
    if st.session_state.quiz_data:
        st.info("모든 문제를 풀고 '전체 정답 제출' 버튼을 눌러주세요.")
