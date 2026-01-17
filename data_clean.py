import pandas as pd
import requests

URL_API = "http://localhost:8080/api/calificaciones"


def cargar_datos() -> pd.DataFrame:
    """
    Carga los datos desde la API y aplana la estructura JSON (Calificaciones).
    """
    try:
        response = requests.get(URL_API)
        response.raise_for_status()
        datos_raw = response.json()

        lista_procesada = []

        for item in datos_raw:
            # Manejo seguro de diccionarios anidados con .get()
            usuario = item.get("usuario") or {}
            platillo = item.get("platillo") or {}

            fila = {
                "id_calificacion": item.get("idCalificacion"),
                "puntuacion": item.get("puntuacion"),
                "comentario": item.get("comentarioCorto"),
                "cliente": usuario.get("nombreCompleto"),
                "email_cliente": usuario.get("email"),
                "nombre": platillo.get("nombre"),
                "precio": platillo.get("precio"),
            }
            lista_procesada.append(fila)

        return pd.DataFrame(lista_procesada)
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return pd.DataFrame()


def manejar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rellena valores nulos con valores por defecto.
    """
    df_procesado = df.copy()

    # Columnas de texto
    cols_texto = ["comentario", "cliente", "email_cliente", "nombre"]
    for col in cols_texto:
        if col in df_procesado.columns:
            df_procesado[col] = df_procesado[col].fillna("Desconocido")

    # Columnas numéricas
    if "puntuacion" in df_procesado.columns:
        df_procesado["puntuacion"] = df_procesado["puntuacion"].fillna(0)

    if "precio" in df_procesado.columns:
        df_procesado["precio"] = df_procesado["precio"].fillna(0.0)

    print("Valores nulos manejados correctamente.")
    return df_procesado


def estandarizar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estandariza texto (strip espacios, mantiene mayúsculas/minúsculas originales).
    Manteniene columnas numéricas intactas para análisis.
    """
    df_procesado = df.copy()

    # Estandarización de texto
    cols_texto = ["comentario", "cliente", "nombre"]
    for col in cols_texto:
        if col in df_procesado.columns:
            # Convertir a string y quitar espacios inicio/fin solamente
            df_procesado[col] = df_procesado[col].astype(str).str.strip()

    print("Texto estandarizado correctamente.")
    return df_procesado


def preparar_dataframe_analisis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por platillo ('nombre') para calcular estadísticas
    necesarias para las gráficas:
    - promedio_calificacion (media de puntuacion)
    - total_votos (conteo de puntuacion)
    - precio (toma el primer valor encontrado)
    """
    if df.empty or "nombre" not in df.columns:
        return pd.DataFrame()

    agrupado = (
        df.groupby("nombre")
        .agg(
            promedio_calificacion=("puntuacion", "mean"),
            total_votos=("puntuacion", "count"),
            precio=("precio", "first"),
        )
        .reset_index()
    )

    return agrupado



def obtener_datos_fidelidad():
    # Asumiendo que consultas el endpoint de calificaciones
    url = "http://localhost:8080/api/calificaciones" 
    try:
        response = requests.get(url)
        datos = response.json()
        
        registros = []
        for cal in datos:
            # Extraemos los datos según tu estructura JSON
            registros.append({
                'usuario_nombre': cal['usuario']['nombreCompleto'],
                'platillo_nombre': cal['platillo']['nombre']
            })
            
        df = pd.DataFrame(registros)
        
        # Agrupamos por usuario y contamos cuántos platillos ÚNICOS ha puntuado
        fidelidad = df.groupby('usuario_nombre')['platillo_nombre'].nunique().reset_index()
        fidelidad.columns = ['Cliente', 'Platillos_Distintos']
        
        # Ordenamos de mayor a menor
        return fidelidad.sort_values(by='Platillos_Distintos', ascending=False)
        
    except Exception as e:
        print(f"Error procesando fidelidad: {e}")
        return pd.DataFrame()