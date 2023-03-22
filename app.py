# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:19:45 2023

@author: HP
"""

import speech_recognition as sr
import streamlit as st


def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.write('Speak now...')
        #st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.write('Transcribing')
        #st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            st.write(text)
        except:
            return "Sorry, I did not get that."
        
transcribe_speech()