import streamlit as st
 
st.title('카이팅 지수로 보는 원딜 ')
 
# 탭 레이아웃 생성
tabs = st.tabs(['카이팅 지수', '코드설명', '일반인 VS 프로 분석결과', '특이한 선수', '결론 및 결과'])
 
# 첫 번째 탭에 내용 추가
with tabs[0]:
    st.header('카이팅 지수란?')
    st.subheader("챔피언에게 가한 피해량 / 받은 피해량")
    st.write('챔피언에게 가한 피해량/받은 피해량')
    # 배경 설명: 롤에서 중요한 능력 중 하나가 얼마나 많이 피하고 많이 때렸는지라고 생각합니다.
    # 그래서 챔피언에게 가한 피해량을 받은 피해량으로 나눈 카이팅 지수를 생각 해 봤습니다.
    # 그리고 이 수치는 탱이나 유틸성이 중요한 포지션 보다 원거리 딜러에게 가장 중요한 수치라고 생각 해서 원거리 딜러를 대상으로 카이팅 지수를 구하기로 결정 했습니다.
 
# 두 번째 탭에 내용 추가
with tabs[1]:
    st.header('코드')
    st.write('코드 내용')
    # 닉네임을 입력하면, 닉네임으로 puuid를 조회합니다. 그리고 puuid로 최근 게임 100개를 조회하고 해당 게임들의 matchid를 저장합니다.
    # 100개의 match아이디에 대해서 게임 내부기록을 조회합니다. 이 부분에서 너무 많은 요청을 한다고 에러가 나서 1~2초 랜덤하게 대기시간을 주었습니다.
    # 100개의 게임 중 teamPosition이 원거리 딜러인 게임에 대해서 카이팅 수치를 구하고 평균을 계산합니다
# 세 번째 탭에 내용 추가
with tabs[2]:
    st.header('일반인 vs 프로 분석결과')
    st.write('이것은 탭 3의 내용입니다.')
    # 프로와 일반인을 무작위적으로 조사했습니다. 프로는 op.gg에서 게임중인 프로 관전하기에서 게임중인 사람과 LCK에서 본사람을 무작위로 선택했고
    # 일반인은 상위 30% 티어인 골드1 구간을 조사했습니다. 게임을 꾸준히 즐기고 실력이 평균은 되는 대상을 조사하기 위함입니다. 상위티어 유저의 부캐를 걸러내기위해 여러 시즌동안 비슷한 티어를 유지한 사람을 조사했습니다
    # 프로의 평균은 기록하는반면 일반인의 평균은 인걸 볼 수 있습니다. 이 결과를 통해 카이팅지수가 실력과 관계가 있는 수치임을 알 수 있습니다
  
# 네 번째 탭에 내용 추가
with tabs[3]:
    st.header('인사이트 얻기')
    st.write('광동 태윤의 지표.')
    # 광동의 태윤 선수가 다른 선수들에 비해 지표가 엄청 높았습니다. 이를 기반으로 이 선수의 행보를 추척 해 보았습니다.
    # 논란: LCK 서머 전체 선수 중 데스 1위. 데스 순위권은 탑, 서폿 포지션이라 더욱 이슈가 되고있다.
    # 긍정: 전문가들 사이에서 기대주로 꼽혀왔다.
    # 2022년 12월 2일 한상용 전 감독이 개인 방송에서 밝힌 바에 따르면 이번 스토브 때 생각보다 인기가 많았다. LCK내 다른 팀이나 LPL팀에서도 오퍼가 왔었다. 
    # 광동 프릭스의 감독인 씨맥이 광동과 T1의 경기에서 패배 이후 인터뷰에서 '태윤이 잘한다고 생각한다. 스크림도 잘하고 솔로 랭크도 잘한다'라고 하며 믿음을 보여줬다.
    # LCK에서 2023시즌 최초 펜타킬 달성

# 다섯번째 탭에 내용 추가
with tabs[3]:
    st.header('탭 3')
    st.write('이것은 탭 3의 내용입니다.')
