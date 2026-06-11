import streamlit as st

# 앱 제목 설정
st.title('미사강변 상담실')

# 상담 목록 정의
counsel = ['학교폭력', '진로', '친구관계', '학업 스트레스']

# 세션 상태(Session State)를 이용해 신청된 목록을 저장 (페이지가 새로고침되어도 데이터 유지)
if 'apply' not in st.session_state:
    st.session_state.apply = []

st.subheader('ℹ️ 상담 프로그램 안내')
# 상담 목록을 화면에 예쁘게 출력
for i, item in enumerate(counsel):
    st.write(f"**{i+1}.** {item}")

# 사용자 선택 (라디오 버튼)
choice = st.radio("원하는 상담 프로그램을 선택하세요:", counsel)

# 신청 버튼
if st.button('신청하기'):
    st.session_state.apply.append(choice)
    st.success(f'🎉 [{choice}] 신청완료!')

# 신청된 목록 출력
st.markdown('---')
st.subheader('📋 나의 신청 목록')
if st.session_state.apply:
    for item in st.session_state.apply:
        st.write(f"- {item}")
else:
    st.info("아직 신청한 상담이 없습니다.")