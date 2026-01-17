import pandas as pd
import requests

URL_API = "http://localhost:8080/api/calificaciones"


def cargar_datos() -> pd.DataFrame:
    """
    Carga los datos desde la API y los retorna como un DataFrame.
    """
    try:
        response = requests.get(URL_API)
        response.raise_for_status()
        datos_raw = response.json()
        
        lista_procesada = []
        
        for p in datos_raw:
            # Extraemos las puntuaciones de la lista anidada
            puntuaciones = [c['puntuacion'] for c in p.get('calificaciones', [])]
            
            # Calculamos el promedio (si no hay calificaciones, ponemos 0)
            promedio = sum(puntuaciones) / len(puntuaciones) if puntuaciones else 0
            
            lista_procesada.append({
                'nombre': p['nombre'],
                'precio': p['precio'],
                'promedio_calificacion': promedio,
                'total_votos': len(puntuaciones)
            })
            
        return pd.DataFrame(lista_procesada)
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()


def manejar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Maneja los valores nulos en el DataFrame usando dropna para eliminar datos críticos o faltantes
    y fillna para reemplazar los valores nulos de una columna por una cadena de texto.
    """
    df_procesado = df.copy()
    print("\nManejo de valores nulos:")

    filas_iniciales = len(df_procesado)
    df_procesado.dropna(subset=['Texto', 'Sentimiento'], inplace=True)
    eliminadas = filas_iniciales - len(df_procesado)
    print(f"Filas eliminadas: {eliminadas} filas (datos criticos faltantes en el texto, sentimiento o autor)")#Se eliminan filas con datos criticos faltantes

    df_procesado['Sentimiento'].fillna('No clasificado', inplace=True) # Rellena valores nulos en 'Sentimiento' con 'No clasificado'
    df_procesado['Longitud_Caracteres'].fillna(0, inplace=True) # Rellena valores nulos en 'Longitud_Caracteres' con 0
    df_procesado['Fuente/Autor'].fillna('No clasificado', inplace=True) # Rellena valores nulos en 'Fuente/Autor' con 'No clasificado'


    print("Se rellenó 'Sentimiento' con 'No clasificado' y 'Longitud_Caracteres' con 0")
    print("Se rellenó 'Fuente/Autor' con 'No clasificado'")
    print(f"Total de filas: {len(df_procesado)}")
    print("\nManejo de valores nulos completado")
    return df_procesado
    



def estandarizar_texto(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Estandariza una columna de texto, convirtiendo a minúsculas y eliminando
    espacios extra, reemplazando los espacios en blanco por un solo espacio.
    """

    df_procesado = df.copy() #Siempre en cada función se crea una copia del DataFrame original.
    print(f"\nEstandarizando la columna '{columna}'...")

    if df_procesado[columna].dtype == 'object':
        df_procesado[columna] = df_procesado[columna].str.lower() #Se convierte a minúsculas

        df_procesado[columna] = df_procesado[columna].str.strip() #Se eliminan espacios extra
        
        df_procesado[columna] = df_procesado[columna].str.replace(r'\s+', ' ', regex=True) #Se reemplazan los espacios en blanco por un solo espacio

        print(f"Columna '{columna}' unificada a minúsculas y espacios extra eliminados con éxito")
    else:
        print(f"La columna '{columna}' tiene dtype='{df_procesado[columna].dtype}' (no 'object')")
        print("Solo se pueden estandarizar columnas de tipo 'object' (texto). Columna omitida.")  
    
    print("\nEstandarización completada")
    return df_procesado




def limpieza_especifica(df: pd.DataFrame) -> pd.DataFrame:
    """
    Función de limpieza específica (eliminar símbolos y recalcular longitud).
    """
    df_procesado = df.copy()
    
    print("\n[LIMPIEZA ESPECÍFICA DE METADATOS]")
    
    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].astype(str).str.replace(r'[$,!"]', '', regex=True)
    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].str.strip()
    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].str.lower()
    print("- Símbolos especiales eliminados y convertido a minúsculas en 'Fuente/Autor'.")
    
    df_procesado['Longitud_Caracteres'] = df_procesado['Texto'].astype(str).str.len()
    print("- Recalculada la 'Longitud_Caracteres' basándose en el texto limpio.")
    
    print("Limpieza específica completada.")
    
    return df_procesado 