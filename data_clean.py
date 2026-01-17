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
                "platillo": platillo.get("nombre"),
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
    cols_texto = ["comentario", "cliente", "email_cliente", "platillo"]
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
    1. Estandariza texto (strip espacios, mantiene mayúsculas/minúsculas originales).
    2. Formatea el precio con signo de dolar ($).
    """
    df_procesado = df.copy()

    # Estandarización de texto
    cols_texto = ["comentario", "cliente", "platillo"]
    for col in cols_texto:
        if col in df_procesado.columns:
            # Convertir a string y quitar espacios inicio/fin solamente
            df_procesado[col] = df_procesado[col].astype(str).str.strip()

    # Formateo de precio con $
    if "precio" in df_procesado.columns:
        # Aseguramos que sea float para el formateo, luego a string
        df_procesado["precio"] = df_procesado["precio"].apply(
            lambda x: f"$ {float(x):.2f}" if pd.notnull(x) else "$ 0.00"
        )

    print("Texto estandarizado y precios formateados.")
    return df_procesado


if __name__ == "__main__":
    # Bloque de prueba
    df = cargar_datos()
    if not df.empty:
        df = manejar_nulos(df)
        df = estandarizar_datos(df)
        print("\nDataFrame Resultante:")
        print(df.tail())
    else:
        print("No se pudieron cargar datos para la prueba.")
