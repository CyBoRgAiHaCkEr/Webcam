import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import logging

# This stops the log spam that can crash the browser tab
logging.basicConfig(level=logging.ERROR)

st.title("Webcam: Final Stability Mode")

# Using only the most reliable Google STUN servers
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302", "stun:stun1.l.google.com:19302"]}]}
)

try:
    webrtc_streamer(
        key="stability-v3",
        rtc_configuration=RTC_CONFIGURATION,
        # Force a lower resolution to prevent network timeout restarts
        media_stream_constraints={
            "video": {"width": {"ideal": 640}, "height": {"ideal": 480}},
            "audio": False 
        },
        async_processing=True,
    )
except Exception as e:
    st.error(f"A technical error occurred: {e}")
    st.info("Try refreshing the page or checking your camera privacy settings.")

st.write("---")
st.caption("If this restarts, the issue is likely a browser extension (like an AdBlocker) interfering with the WebRTC handshake.")
