import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

st.title("Webcam Fix: Relay Protocol 🎥")

RTC_CONFIGURATION = RTCConfiguration(
    {
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {
                "urls": ["turn:openrelay.metered.ca:443"],
                "username": "openrelayproject",
                "credential": "openrelayproject", # Changed from password to credential
            },
        ]
    }
)

webrtc_streamer(
    key="final-attempt",
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
