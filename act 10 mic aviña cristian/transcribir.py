import speech_recognition as sr

filename = "audio.wav"
output_file = "transcripcion.txt"

r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:

        print("Procesando el archivo de audio...")

        audio_data = r.record(source)

        text = r.recognize_google(audio_data, language="es-ES")

        print("Texto reconocido:")
        print(text)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Transcripción guardada en {output_file}")

except FileNotFoundError:
    print(f"Archivo {filename} no encontrado.")

except sr.UnknownValueError:
    print("No se pudo entender el audio.")

except sr.RequestError as e:
    print(f"Error con Google Speech Recognition: {e}")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")