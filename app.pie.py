import streamlit as st

st.header("Hello")
st.header("소윤")
st.write("정연이랑 같이 놀자")
import streamlit as st

st.title("은선이의 옷가게")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    import streamlit as st

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
Copy
