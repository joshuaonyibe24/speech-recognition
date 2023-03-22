# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:38:14 2023

@author: HP
"""

import streamlit as st
import speech_recognition as sr
from app import transcribe_speech


def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        transcribe_speech()
        #st.write("Transcription: ", text)
        
        
if __name__ == "__main__":
    main()