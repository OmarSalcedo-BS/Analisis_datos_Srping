import matplotlib.pyplot as plt
import seaborn as sns
import os



def graficar_raking_calidad(df, folder="resultados"):
    """
    Genera un gráfico de barras apiladas para visualizar la distribución de calificaciones
    por platillo.

    Args:
        df (pd.DataFrame): DataFrame con las columnas 'platillo' y 'puntuacion'.
        folder (str): Carpeta donde se guardará el gráfico.
    """

    # Crea la carpeta si esta no existe en el sistema
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = f"{folder}/rakingCalidad.png"

    plt.figure(figsize=(10, 6))
    # Ordenamos de mejor a peor
    df_sorted = df.sort_values(by="promedio_calificacion", ascending=False)

    sns.barplot(data=df_sorted, x="promedio_calificacion", y="nombre", palette="magma")

    plt.title("Raking de calidad de los platillos")
    plt.xlim(0, 5)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


def graficar_precio_vs_calidad(df, folder="resultados"):
    """
    Genera un gráfico de dispersión para visualizar la relación entre el precio y la calificación promedio de los platillos.

    Args:
        df (pd.DataFrame): DataFrame con las columnas 'precio', 'promedio_calificacion' y 'total_votos'.
        folder (str): Carpeta donde se guardará el gráfico.
    """

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = f"{folder}/precio_vs_calidad.png"
    plt.figure(figsize=(12, 8))

    sns.scatterplot(
        data=df, 
        x='precio', 
        y='promedio_calificacion', 
        size='total_votos',      # Puntos más grandes = más popular
        hue='promedio_calificacion', # Cambia de color según la nota
        palette='viridis',       # Escala de colores elegante
        sizes=(100, 1000),       # Rango de tamaño de los puntos
        alpha=0.7                # Transparencia para ver puntos encimados
    )

    for i in range(df.shape[0]):
        plt.text(
            df.precio[i]+0.2,
            df.promedio_calificacion[i],
            df.nombre[i],
            fontsize=9,
            alpha=0.8
        )

    plt.axhline(df['promedio_calificacion'].mean(), color='red', linestyle='--', alpha=0.5, label='Promedio Notas')
    plt.axvline(df['precio'].mean(), color='blue', linestyle='--', alpha=0.5, label='Promedio Precio')

    plt.title('Matriz de Valor: Precio vs. Calificación Promedio', fontsize=16)
    plt.xlabel('Precio ($)', fontsize=12)
    plt.ylabel('Calificación (1-5 Estrellas)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


def graficar_clientes_frecuentes(df, folder="resultados", output_path='resultados/clientes_frecuentes.png'):
    plt.figure(figsize=(10, 6))
    
    # Tomamos solo los top 10 para que no se amontone el gráfico
    top_10 = df.head(10)
    
    sns.barplot(
        data=top_10, 
        x='Platillos_Distintos', 
        y='Cliente', 
        palette='viridis'
    )
    
    plt.title('Top 10 Clientes: Diversidad de Experiencia en el Menú', fontsize=14)
    plt.xlabel('Número de Platillos Diferentes Calificados')
    plt.ylabel('Nombre del Cliente')
    
    # Aseguramos que el eje X use números enteros
    plt.xticks(range(0, int(top_10['Platillos_Distintos'].max()) + 1))
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return output_path

