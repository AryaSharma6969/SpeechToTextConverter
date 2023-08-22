import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech-to-Text App")
    st.write("Click below the Start Recording button, record your speech and see the text!")

    recognizer = sr.Recognizer()

    # Add a button to start recording
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)

        # Convert speech to text
        try:
            text = recognizer.recognize_google(audio)
            st.write("Text:", text)
        except sr.UnknownValueError:
            st.write("Oops! Speech recognition could not understand audio.")
        except sr.RequestError as e:
            st.write("Oops! Could not request results from Speech Recognition service; {0}".format(e))
if __name__ == "__main__":
    main()
