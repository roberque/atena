# Our main file.

import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

# Abrir o microfone para captura
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(s)
    while True:
  audio = r.listen(source) # Define microfone python como fonte de audio

   speech = r.recognize_google(audio,language='pt')
   print('Você disse:', speech)