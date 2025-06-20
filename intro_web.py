import streamlit as st
from openai import OpenAI

# API 키 입력
client = OpenAI(api_key="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")

# 웹페이지 타이틀
st.title("📄 AI 자기소개서 생성기")

# 입력값 받기
job = st.text_input("지원 직무를 입력하세요:")
strength = st.text_input("당신의 강점은?")
experience = st.text_area("경험을 간단히 설명해 주세요:")

# 버튼 누르면 실행
if st.button("자기소개서 생성"):
    with st.spinner("AI가 글을 작성 중입니다..."):
        prompt = f"""
다음 정보를 바탕으로 자기소개서를 작성해줘.
문단은 다음 항목 순서로 구성해줘:
1. 성장 과정
2. 성격의 장단점
3. 지원 동기
4. 입사 후 포부

요청사항:
- 각 문단은 **8~9줄 이상**으로 충분히 상세하게 작성해줘.
- **"저는", "저의", "제가","제"**로 시작하는 문장은 피하고, **다양한 표현 방식**으로 글을 시작해줘.
- 자연스럽고 논리적인 흐름을 유지하며, 사례와 경험을 풍부하게 포함해줘.

입력 정보:
지원 직무: {job}
강점: {strength}
경험: {experience}
"""


        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        st.success("✅ 자기소개서가 생성되었습니다!")
        st.markdown(result)
