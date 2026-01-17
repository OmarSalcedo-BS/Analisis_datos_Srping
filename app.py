import os
import pandas as pd
from data_clean import (
    cargar_datos,
    manejar_nulos,
    estandarizar_datos,
    preparar_dataframe_analisis,
    obtener_datos_fidelidad,
)
from visualizacion import (
    graficar_raking_calidad,
    graficar_precio_vs_calidad,
    graficar_clientes_frecuentes,
)


"""
Momento 3 -  Fecha límite enero 22 de enero.
Construir una aplicación de análisis de datos en Python. 
Este tomará datos de la api desarrollada en Spring Boot
para hacer analisis de datos sobre el restaurante
En mi caso usaré las puntuaciones y platillos para crear graficas
de platillos mejor puntuados contra los peores.

"""


def limpiar_consola():
    """
    Limpia la consola se considera una buena práctica por eso la estoy
    creando aquí como una adición de parte de mi curso de Platzi
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def generar_reporte():
    """
    Genera el reporte completo de análisis de datos.
    """
    limpiar_consola()
    df = cargar_datos()

    if df.empty:
        print("No se pudieron cargar los datos.")
        return

    df = manejar_nulos(df)
    df = estandarizar_datos(df)

    # Preparar DataFrame para análisis (agrupado por platillo)
    df_analisis = preparar_dataframe_analisis(df)

    if df_analisis.empty:
        print("No hay datos suficientes para el análisis.")
        return

    img_raking = graficar_raking_calidad(df_analisis)
    img_preciovscalidad = graficar_precio_vs_calidad(df_analisis)

    # Obtener datso especificos para fidelidad
    df_fidelidad = obtener_datos_fidelidad()
    if df_fidelidad.empty:
        print("No se pudieron cargar datos de fidelidad.")
        # Puedes manejar esto poniendo una imagen por defecto o saltando el paso
        img_clientesFrecuentes = ""
    else:
        img_clientesFrecuentes = graficar_clientes_frecuentes(df_fidelidad)

    # Formatear el precio en el DF original para la tabla (solo visualización)
    if "precio" in df.columns:
        df["precio"] = df["precio"].apply(
            lambda x: f"$ {float(x):.2f}" if pd.notnull(x) else "$ 0.00"
        )

    tabla_html = df.to_html(
        classes="display shadow", table_id="tabla_analisis", index=False
    )

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte Sabor Urbano</title>
        <link rel="stylesheet" href="estilos.css">
        <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
    </head>
    <body>
        <h1>Reporte de Análisis Del restaurante</h1>
        
        <div class="container-graficos">
            <div class="card">
                <h3>Ranking de Calidad</h3>
                <img src="{img_raking}" width="100%">
            </div>
            <div class="card">
                <h3>Análisis de Precio</h3>
                <img src="{img_preciovscalidad}" width="100%">
            </div>
            <div class="card">
                <h3>Análisis de Clientes Frecuentes</h3>
                <img src="{img_clientesFrecuentes}" width="100%">
            </div>
        </div>

        <h2>Detalle de los Datos</h2>
        <div class="container-tabla">
            {tabla_html}
        </div>

        <script src="https://code.jquery.com/jquery-3.7.0.js"></script>
        <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
        <script>
            $(document).ready(function() {{
                $('#tabla_analisis').DataTable();
            }});
        </script>
    </body>
    </html>
    """

    with open("reporte.html", "w", encoding="utf-8") as f:
        f.write(html_template)


if __name__ == "__main__":
    generar_reporte()
