import speech_recognition as sr

r = sr.Recognizer()

def listar_dispositivos():
    dispositivos = sr.Microphone.list_microphone_names()

    for index, name in enumerate(dispositivos):
        print(f"{index}: {name}")

def SpeechToText(device_index):

    with sr.Microphone(device_index=device_index) as source:

        print("Habla ahora...")

        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="es-ES")

            print("Texto reconocido:")
            print(texto)

            with open("transcripcion.txt", "w", encoding="utf-8") as archivo:
                archivo.write(texto)

            print("Texto guardado en transcripcion.txt")

        except sr.UnknownValueError:
            print("No se pudo entender el audio.")

        except sr.RequestError as e:
            print(f"Error con el servicio de Google: {e}")

print("Dispositivos disponibles:")

listar_dispositivos()

indice_mic = int(input("Elige el índice del micrófono que deseas usar: "))

SpeechToText(device_index=indice_mic)