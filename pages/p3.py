import streamlit as st 
st.set_page_config(page_title='page3', page_icon=':smily:')
st.title('3페이지 입니다^^')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
import streamlit as st
# 폰트 설정
rc("font", family="Malgun Gothic")
# 마이너스 기호 깨짐 해결
rc('axes', unicode_minus=False)
st.title("매 사전과 비둘기 사전")
data1 = pd.read_csv('all_dic.csv')
df1 = pd.DataFrame(data1)
st.dataframe(df1)
st.subheader('Hawikish vs Dovish 단어 개수 비교')
# polarity 값 카운트
plrty = df1['polarity'].value_counts()
# 바 플롯 생성
x = np.arange(2)
bar = plt.bar(x, plrty, color=["coral", "cornflowerblue"], width=0.5)
plt.xticks(np.arange(2), labels=['Hawikish', 'Dovish'])
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.0f' % height, ha='center', va='bottom', size=12)
# 플롯을 Streamlit에 표시
st.pyplot(plt)
data2 = pd.read_csv('문서톤과 기준금리.csv')
del data2['Unnamed: 0']
df2 = pd.DataFrame(data2)
st.download_button(label='파일 다운로드', data=df2.to_csv(), file_name='tone_baseRate.csv')
# 날짜 형식을 datetime 형식으로 변환
df2['date'] = pd.to_datetime(df2['date'])
# 데이터 프레임 출력
st.dataframe(df2)
st.subheader('일자별 기준금리 변화')
fig, ax = plt.subplots()
ax.plot(df2['date'], df2['base_rate'])
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.set_ylabel('base_rate')
# 그래프 배경 색상 설정
plt.gca().set_facecolor('white')  # 축의 배경을 흰색으로 설정
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
user_input = st.date_input('조회 일자 입력: ', pd.to_datetime('2005-06-09'))
# 입력받은 날짜의 기준금리 출력
input_date = pd.to_datetime(user_input)
# 날짜 형식을 맞추기 위해 일치하는 행을 찾기
rate = df2.loc[df2['date'].dt.date == input_date.date(), 'base_rate'].values
if rate.size > 0:
    st.write(f'{input_date.date()}의 기준금리는 {rate[0]}입니다.')
else:
    st.write('해당 날짜의 기준금리를 찾을 수 없습니다.')