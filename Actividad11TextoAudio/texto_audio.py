# Actividad 11
# Convertir texto en audio utilizando Python
# Librería utilizada: gTTS

from gtts import gTTS

texto = "Arriba las chivas."

audio = gTTS(text=texto, lang='es')

audio.save("audio.mp3")

print("Audio generado correctamente")