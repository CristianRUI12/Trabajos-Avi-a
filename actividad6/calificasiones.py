import random
import csv

# Lista de 10 alumnos con nombre y apellido paterno
alumnos = [
    "Diego Navarro",
    "Valentina Cruz",
    "Fernando Castillo",
    "Camila Ortega",
    "Ricardo Vega",
    "Paola Ríos",
    "Andrés Mendoza",
    "Daniela Salazar",
    "Héctor Paredes",
    "Renata Fuentes"
]

# Lista de 5 materias
materias = ["Matematicas", "Espanol", "Ciencias", "Historia", "Ingles"]

def generar_calificaciones():
    # Diccionario para almacenar las calificaciones de cada alumno
    datos_alumnos = {}
    
    for alumno in alumnos:
        # Generar una calificación aleatoria entre 5.0 y 10.0 para cada materia
        calificaciones = {materia: round(random.uniform(5.0, 10.0), 1) for materia in materias}
        datos_alumnos[alumno] = calificaciones
        
    return datos_alumnos

def guardar_csv(datos, nombre_archivo="calificaciones.xlsx"):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        
        # Escribir encabezado
        encabezado = ["Alumno"] + materias + ["Promedio"]
        escritor.writerow(encabezado)
        
        # Escribir filas de alumnos
        for alumno, calificaciones in datos.items():
            fila = [alumno]
            suma = 0
            for materia in materias:
                calif = calificaciones[materia]
                fila.append(calif)
                suma += calif
            
            promedio = round(suma / len(materias), 1)
            fila.append(promedio)
            escritor.writerow(fila)
    
    print(f"\nArchivo '{nombre_archivo}' generado con éxito.")

def mostrar_tabla(datos):
    # Definir el ancho de las columnas
    ancho_nombre = 20
    ancho_materia = 12
    
    # Imprimir encabezado
    encabezado = f"{'Alumno':<{ancho_nombre}}"
    for materia in materias:
        encabezado += f"{materia:^{ancho_materia}}"
    encabezado += f"{'Promedio':^{ancho_materia}}"
    
    print("-" * len(encabezado))
    print(encabezado)
    print("-" * len(encabezado))
    
    # Imprimir filas de alumnos
    for alumno, calificaciones in datos.items():
        fila = f"{alumno:<{ancho_nombre}}"
        suma = 0
        for materia in materias:
            calif = calificaciones[materia]
            fila += f"{calif:^{ancho_materia}}"
            suma += calif
        
        promedio = round(suma / len(materias), 1)
        fila += f"{promedio:^{ancho_materia}}"
        print(fila)
    
    print("-" * len(encabezado))

if __name__ == "__main__":
    calificaciones_generadas = generar_calificaciones()
    mostrar_tabla(calificaciones_generadas)
    guardar_csv(calificaciones_generadas)
