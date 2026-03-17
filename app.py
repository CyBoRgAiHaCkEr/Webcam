import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import logging

# Set up logging so we can see what's happening in the background
logging.basicConfig(level=logging.DEBUG)

st.title("Emergency WebRTC Link")

# Simplified config - removing unnecessary parameters that cause hangs
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

ctx = webrtc_streamer(
    key="emergency-link",
    rtc_configuration=RTC_CONFIGURATION,
    # This 'video_html_attrs' fix helps mobile browsers load the feed
    video_html_attrs={
        "style": {"width": "100%"},
        "controls": False,
        "autoPlay": True,
        "playsInline": True,
        "muted": True,
    },
)

if ctx.state.playing:
    st.success("Stream is active!")
else:
    st.info("Press 'Start' to begin the connection.")
