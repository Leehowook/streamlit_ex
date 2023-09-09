import streamlit as st
 
st.title('카이팅 지수로 보는 원딜 ')
 
# 탭 레이아웃 생성
tabs = st.tabs(['카이팅 지수', '코드설명', '일반인 VS 프로 분석결과', '특이한 선수', '결론 및 결과'])
 
# 첫 번째 탭에 내용 추가
with tabs[0]:
    st.header('카이팅 지수란?')
    st.subheader("챔피언에게 가한 피해량 / 받은 피해량")
    st.write('챔피언에게 가한 피해량/받은 피해량')
    #배경 설명: 롤에서 중요한 능력 중 하나가 얼마나 많이 피하고 많이 때렸는지라고 생각합니다.
    #그래서 카이팅 지수를 생각 해 봣고 처음에는 포지션에 상관없이 값을 구해봤습니다.
    #그러다 원딜 포지션에서 가장 큰 관계가 있음을 알았습니다. 그래서 원딜 포지션을 대상으로 카이팅 지수를 구하기로 했습니다.
 
# 두 번째 탭에 내용 추가
with tabs[1]:
    st.header('코드')
    st.code("
    
            ")
    st.write('이것은 탭 2의 내용입니다.')
 
# 세 번째 탭에 내용 추가
with tabs[2]:
    st.header('탭 3')
    st.write('이것은 탭 3의 내용입니다.')
  
# 네 번째 탭에 내용 추가
with tabs[3]:
    st.header('탭 3')
    st.write('이것은 탭 3의 내용입니다.')
