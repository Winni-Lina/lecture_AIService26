import streamlit as st

st.title("사용자 입력 폼 만들기")

with st.container(border=True):
    st.subheader("사용자 입력 폼")
    
    name = st.text_input("이름", placeholder="이름을 입력하세요")
    age = st.number_input("나이", min_value=1, step=1, value=1)
    agreement = st.checkbox("약관에 동의합니다")
    submitted = st.button("제출")

if submitted:
    st.write(f"이름: {name}, 나이: {age}")
    
    if agreement:
        st.success("약관에 동의했습니다.")
    else:
        st.warning("약관 동의가 필요합니다.")