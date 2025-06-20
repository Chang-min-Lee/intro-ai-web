import streamlit as st
import os
from openai import OpenAI, AuthenticationError

# 환경변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# 예외처리로 안정성 확보
try:
    client = OpenAI(api_key=api_key)

    st.title("📄 AI 자기소개서 생성기")

    job = st.text_input("지원 직무를 입력하세요:")
    strength = st.text_input("당신의 강점은?")
    experience = st.text_area("경험을 간단히 설명해 주세요:")

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

except AuthenticationError:
    st.error("❌ API 인증에 실패했습니다. 환경변수 또는 API 키를 확인하세요.")
except Exception as e:
    st.error(f"⚠️ 알 수 없는 오류가 발생했습니다: {str(e)}")
