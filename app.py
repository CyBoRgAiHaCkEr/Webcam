import streamlit as st
from streamlit_webrtc import webrtc_streamer
import logging

# Kill the logs so they don't overflow the server memory
logging.basicConfig(level=logging.CRITICAL)

st.title("Webcam: emergency_safe_mode")

ctx = webrtc_streamer(
    key="FORCE_NEW_ID_99", 
    media_stream_constraints={"video": True, "audio": False},
    # This prevents the 'NoneType' crash you saw in your logs
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    on_change=lambda: None 
)

if ctx.state.playing:
    st.success("Connection established!")
else:
    st.info("Waiting for 'Start' button click...")
