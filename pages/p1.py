import streamlit as st 
st.set_page_config(page_title='page1', page_icon=':smiley:')
st.subheader(':smiley: 1페이지 입니다.')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np 
import re


st.title('금리와 극성점수와의 관계')
data=pd.read_csv('all_dic.csv')
data2=pd.read_csv('문서톤과 기준금리.csv',index_col=0)
data2['date'] = pd.to_datetime(data2['date'])

#data3=pd.read_csv('시각화용2.csv')
#data4=pd.concat([data2,data3['h_list']],axis=1)



    

col1, col2=st.columns(2)
col1.write('<극성 사전>')
col1.dataframe(data)
col2.write('<극성점수 기준금리>')
col2.dataframe(data2)






# Streamlit 앱 설정
st.title('토큰별 분류 성향 알아보기')

# 사용자로부터 검색할 토큰 입력 받기
search_word = st.text_input('찾고싶은 토큰을 입력하세요')

if search_word:
    #정규식 패턴 설정
    pattern = re.compile(f'.*{re.escape(search_word)}.*', flags=re.IGNORECASE)

    # DataFrame에서 정규식 패턴에 맞는 행 필터링
    filtered_data = data[data['word'].str.match(pattern)]

    # 필터링된 결과가 있는 경우에만 처리
    if not filtered_data.empty:
        
        # 하나의 행만 선택 (여기서는 첫 번째 행)
        st.dataframe(filtered_data)
        st.subheader(f'{search_word}단어가 포함된 토큰의 분류 빈도')
        st.bar_chart(filtered_data['polarity'].value_counts())
        col3, col4= st.columns(2)
        
         # 'polarity' 값이 'Hawkish'와 'Dovish'인 행의 개수 비교
        hawkish_count = len(filtered_data[filtered_data['polarity'] == 'Hawikish'])
        dovish_count = len(filtered_data[filtered_data['polarity'] == 'Dovish'])
        data2['h_count'] = data2['h_count'].astype(int)
        data2['d_count'] = data2['d_count'].astype(int)

        # 'Hawkish'와 'Dovish'의 개수 비교하여 데이터 필터링
        if hawkish_count > dovish_count:
            d2 = data2[data2['h_count'] > data2['d_count']]
            t='Hawikish'
        else:
            d2 = data2[data2['h_count'] < data2['d_count']]
            t='Dovish'

        # 결과 데이터를 시각화
        st.subheader(f'{t}가 우세한 기준 금리 추세')
        st.line_chart(d2['base_rate'])
        
        
col3,col4=st.columns(2)
sdt = col3.date_input("시작일자를 선택하세요", pd.to_datetime("2005-01-01"),min_value=pd.to_datetime("2005-01-01"), max_value=pd.to_datetime("2020-12-31"))
edt = col4.date_input("종료일자를 선택하세요", pd.to_datetime("2005-01-01"),min_value=pd.to_datetime("2005-01-01"), max_value=pd.to_datetime("2020-12-31"))  

if sdt and edt:
   
    st.subheader("해당 날짜 별 \'기준금리\'와 \'극성점수\' 변동 추이")
    filtered_data3 = data2[(data2['date'] >= pd.Timestamp(sdt)) & (data2['date'] <=  pd.Timestamp(edt))]
    chart_data = filtered_data3.set_index('date')[['base_rate', 's_score']]
    st.line_chart(chart_data)
    
    
   
st.title('상관관계 표')
corr_coef = np.corrcoef(data2['base_rate'], data2['s_score'])[0, 1]

# Streamlit 앱 설정
st.subheader('<s_core와 base_rate상관 계수>')

# 상관 계수 출력
st.write(f"상관 계수: {corr_coef}")


# Scatter Plot 그리기
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(data2['base_rate'], data2['s_score'])


ax.set_xlabel('base_rate')
ax.set_ylabel('s_score')
ax.set_title('Scatter Plot')

# 그래프를 Streamlit 앱에 추가
st.pyplot(fig)

 
  
st.write('토큰 시각화')
text_data = ' '.join(data['word'].astype(str).tolist())
# 워드클라우드 설정 및 생성
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)


# 워드클라우드 그래프 출력
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Matplotlib 그래프를 Streamlit 앱에 추가
st.pyplot(plt)
    
 
    



