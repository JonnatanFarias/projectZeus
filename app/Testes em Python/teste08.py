import speech_recognition as sr
import os

rec = sr.Recognizer()
with sr.Microphone(device_index=1)as mic:
    rec.adjust_for_ambient_noise(mic)
    audio = rec.listen(mic)
    frase=rec.recognize_google(audio , language="pt-BR")
    comando ="Ok Google"  
if(frase ==comando):
    print("comando aceito")
with sr.Microphone(device_index=1)as mic:
    rec.adjust_for_ambient_noise(mic)
    audio = rec.listen(mic)
    frase=rec.recognize_google(audio , language="pt-BR")
if "navegador" in frase:
      os.system("start Chrome.exe")
else:
    print("comando não aceito")


