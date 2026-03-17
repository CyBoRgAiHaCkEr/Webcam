import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

st.title("Final Fix: Relay Mode 🚀")

# We are adding a TURN server here. 
# This acts as a 'tunnel' through your firewall.
RTC_CONFIGURATION = RTCConfiguration(
    {
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {
                "urls": ["turn:openrelay.metered.ca:443"],
                "username": "openrelayproject",
                "password": "openrelayproject",
            },
        ]
    }
)

webrtc_streamer(
    key="relay-stream",
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False}, # Audio off to reduce lag
    async_processing=True,
)

st.warning("If the screen is still black, please try opening this URL on your phone's mobile data (not Wi-Fi).")
