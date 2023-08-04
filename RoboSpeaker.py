import win32com.client as wincom

while True:
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = input("Enter what you want to speak!")
    if text == "quit":
           break
    speak.Speak(text)