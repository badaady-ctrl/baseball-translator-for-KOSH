import streamlit as st
import google.generativeai as genai

# 1. API 키 설정 (쌍따옴표 " " 사이에 발급받은 키를 꼭! 넣어주세요)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 빠르고 가벼운 모델 사용
model = genai.GenerativeModel('gemini-2.5-flash') 

# 2. 화면 UI 구성 (웹페이지 화면 꾸미기)
st.set_page_config(page_title="야구 용어 번역기", page_icon="⚾")
st.title("⚾ 안타왕 이바다의 야구 용어 번역기")
st.write("고승혜님 이바다가 방금 신나서 떠들어 재낀 알 수 없는 야구 용어를 입력해 보세요!")

# 아내가 입력할 텍스트 창
user_input = st.text_input("예: WAR, WHIP, 바빕신, OPS, 퀄리티스타트 등")

# 3. 번역 버튼을 눌렀을 때 동작할 로직
if st.button("승혜가 알아먹을수 있는 언어로 번역하기"):
    if user_input:
        with st.spinner('이바다 외계어를 해석 중입니다... 🧠'):
            # AI에게 내리는 구체적인 지시사항 (프롬프트)
            prompt = f"""
            너는 10년 넘게 사회인 야구를 하고 직관을 즐기는 야구 광팬 남편을 둔 아내를 위한 유쾌한 통역사야.
            남편이 말한 야구 용어: '{user_input}'
            
            이 용어의 원래 뜻을 아주 짧게 요약하고, 
            이것을 아내의 일상(육아, 가사, 직장생활, 쇼핑, 명절 등)에 빗대어 아주 웃기고 찰떡같이 공감가게 설명해줘.
            
            출력 형식은 딱 아래와 같이 2줄로 해줘:
            - ⚾ 사전적 의미: (간단하게)
            - 👩‍🏫 일상 비유: (웃기고 공감가게, 세이버메트릭스 수치가 높고 낮음의 의미도 포함해서)
            """
            
            # Gemini API 호출 및 결과 출력
            response = model.generate_content(prompt)
            st.success("번역 완료!")
            st.write(response.text)
    else:
        st.warning("야구 용어를 먼저 입력해 주세요!")

