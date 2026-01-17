import matplotlib.pyplot as plt
import seaborn as sns
import os

def graficar_raking_calidad(df, folder = 'resultados'):
    """
    Genera un gráfico de barras apiladas para visualizar la distribución de calificaciones
    por platillo.

    Args:
        df (pd.DataFrame): DataFrame con las columnas 'platillo' y 'puntuacion'.
        folder (str): Carpeta donde se guardará el gráfico.
    """

    #Crea la carpeta si esta no existe en el sistema
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = f"{folder}/rakingCalidad.png"

    plt.figure(figsize=(10, 6))
    #Ordenamos de mejor a peor
    df_sorted = df.sort_values(by='promedio_calificacion', ascending=False)

    sns.barplot(data = df_sorted, x = 'promedio_calificacion', y = 'nombre', palette = 'magma')

    plt.title('Raking de calidad de los platillos')
    plt.xlim(0, 5)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


def graficar_precio_vs_calidad(df, folder='assets'):
    path = f"{folder}/precio_vs_calidad.png"
    plt.figure(figsize=(10, 6))
    
    sns.scatterplot(data=df, x='precio', y='promedio_calificacion', size='total_votos', hue='nombre', legend=False)
    
    plt.title('Relación Precio vs. Calificación')
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path

    



 
    