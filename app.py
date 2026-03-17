import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

st.set_page_config(page_title="Webcam Mirror", layout="wide")

st.title("Streamlit Live Link 🎥")
st.write("Connect your webcam and audio below. Share the URL to view from another device.")

# Google's public STUN servers allow the connection to bypass firewalls
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

webrtc_streamer(
    key="live-stream",
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": True},
    async_processing=True,
)
