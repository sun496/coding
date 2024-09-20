import streamlit as st
import random

#게임결과 내는 함수. guess는 사람의 추측 값 0(앞면),1(뒷면)
def playGame(guessNum):
comNum=random.randint(0,1)

 if comNum==guessNum:
    st.write('적중')

else:
   st.write('아쉽네연')


st.title('동전 던지기 게임')
st.divider()
st.image('asserts/coin_head.png')
st.image('asserts/coin_tail.png')

st.header('환영한다,빨리 동전이나 굴려라')
st.subheader('앞면일까요? 뒷면일까요?')

if.button('앞면'):
   playGame(0)

if.button('뒷면'):
   playGame(1)

