import os
import sys

def es_archivo_importante(nombre_archivo):
    """Verifica si un archivo tiene una extensión relevante para un proyecto ASP.NET Core Web API."""
    extensiones_importantes = [
        '.cs', '.csproj', '.sln', '.json', '.xml', '.razor'
    ]
    return os.path.splitext(nombre_archivo)[1].lower() in extensiones_importantes

def documentar_codigo(directorio_a_documentar, nombre_archivo_salida):
    """Genera documentación de archivos importantes dentro de un proyecto ASP.NET Core Web API."""
    if not os.path.isdir(directorio_a_documentar):
        print(f"Error: El directorio '{directorio_a_documentar}' no existe.")
        return None

    directorio_script = os.path.dirname(os.path.abspath(__file__))
    if not nombre_archivo_salida.lower().endswith('.txt'):
        nombre_archivo_salida += '.txt'
    archivo_salida = os.path.join(directorio_script, nombre_archivo_salida)

    with open(archivo_salida, 'w', encoding='utf-8') as archivo_txt:
        for root, _, files in os.walk(directorio_a_documentar):
            estructura_directorio = os.path.relpath(root, directorio_a_documentar)
            estructura_directorio = estructura_directorio.replace(os.sep, " > ")

            for file in files:
                archivo_txt.write(f'Estructura: {estructura_directorio}\n')
                archivo_txt.write(f'Archivo: {file}\n')
                archivo_txt.write('-' * 50 + '\n')

                if es_archivo_importante(file):
                    path_completo = os.path.join(root, file)
                    try:
                        with open(path_completo, 'r', encoding='utf-8') as codigo:
                            archivo_txt.write(codigo.read())
                    except Exception as e:
                        archivo_txt.write(f"Error al leer el archivo: {str(e)}\n")
                else:
                    archivo_txt.write(f"[Archivo no incluido en la documentación detallada: {file}]\n")

                archivo_txt.write('\n\n')

    return archivo_salida

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("No se proporcionaron argumentos suficientes. Se solicitará la información necesaria.")
        directorio_a_documentar = input("Ingrese la ruta completa del directorio a documentar: ").strip()
        nombre_archivo_salida = input("Ingrese el nombre del archivo de salida (se añadirá .txt si es necesario): ").strip()
    else:
        directorio_a_documentar = sys.argv[1]
        nombre_archivo_salida = sys.argv[2]

    archivo_salida = documentar_codigo(directorio_a_documentar, nombre_archivo_salida)
    if archivo_salida:
        print(f"Documentación completa. Revisa el archivo {archivo_salida}")
    else:
        print("No se pudo completar la documentación.")
