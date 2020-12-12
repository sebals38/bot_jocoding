import pyttsx3 as tts3

def t2s(text):
    t2s = tts3.init()
    t2s.setProperty('rate', 150)
    t2s.setProperty('volume', 1.0)
    t2s.say(text)
    t2s.runAndWait()
    t2s.stop()


t2s('당신은 지금 HTS를 만들고 있나요?')
# t2s("How's everything going?")