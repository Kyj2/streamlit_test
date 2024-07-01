import streamlit as st  
import pandas as pd
st.set_page_config(page_title="홈페이지", page_icon=":sunglasses:")
st.title('금리 예측 프로젝트 입니다.')
st.header('\'텍스트 마이닝을 활용한 통화정책 논문 구현 프로젝트\'')

st.write(':rocket: p1 에서는 각 단어가 포함된 토큰의 분류 성향과,상관관계,  년도별 기준금리와 의사록 문서 톤 점수를 그래프로 볼 수 있습니다.' )

st.write(':rocket: p2에서는 날짜별, 금리의 up, down별로 기사 데이터를 필터링하여 볼 수 있습니다.')

st.write(':rocket: p3에서는 비둘기와, 매 사전별 비교를 하고 일자를 검색하여 기준금리를 확인 할 수 있습니다.')

