import streamlit as st
from streamlit_webrtc import webrtc_streamer

# Total reset of the component key
webrtc_streamer(key="SUPER_RESET_QUICK", media_stream_constraints={"video": True, "audio": False})
