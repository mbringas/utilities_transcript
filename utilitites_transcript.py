# -*- coding: utf-8 -*-
"""
Utilidades desgrabado
"""

#Write the name of the mp3 files you want to transcribe. e.g. for file Baila_Morena.mp3 and Tu_Gatita.mp3 , list of files
#should be
#     list_of_files=["Baila_Morena","Tu_Gatita"]
list_of_files=[]

!pip install git+https://github.com/openai/whisper.git

import whisper
model = whisper.load_model("turbo")

for i in list_of_files:
  result = model.transcribe(f"{i}.mp3")
  print(result["text"])
  with open(f"transcript_{i}.txt", "a") as f:
    print(result["text"], file=f)
  from google.colab import files
  files.download(f'transcript_{i}.txt')
