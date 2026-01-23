🍽️ Restaurante Sabor Urbano – Análisis de Datos con Python y Spring Boot
📌 Descripción General

Este proyecto consiste en una aplicación de análisis de datos en Python que consume información desde una API REST desarrollada en Spring Boot, procesa los datos y genera visualizaciones y un reporte HTML interactivo.

El sistema funciona de manera integrada:

Spring Boot expone los datos del restaurante mediante endpoints REST.

Python consume estos endpoints para:

Limpiar y preparar los datos

Realizar análisis estadísticos

Generar gráficos

Construir un reporte visual en HTML

⚠️ Importante:
La API REST de Spring Boot debe estar ejecutándose previamente para que el análisis en Python funcione correctamente.

🎯 Objetivos del Proyecto

Consumir datos reales desde una API REST

Aplicar técnicas de limpieza y transformación de datos

Analizar calificaciones, precios y comportamiento de clientes

Generar visualizaciones estadísticas claras

Presentar resultados mediante un reporte HTML profesional

🧩 Arquitectura del Proyecto
Spring Boot (API REST)
        ↓
   Requests (Python)
        ↓
 Limpieza y Análisis
        ↓
 Visualizaciones
        ↓
   Reporte HTML

🗂️ Estructura del Proyecto
Analisis_datos_Spring/
│
├── app.py                  # Script principal
├── data_clean.py           # Limpieza y preparación de datos
├── visualizacion.py        # Generación de gráficos
├── estilos.css             # Estilos del reporte HTML
├── requirements.txt        # Dependencias del proyecto
├── resultados/             # Gráficos y reporte generado
│   ├── rankingCalidad.png
│   ├── precio_vs_calidad.png
│   ├── clientes_frecuentes.png
│   └── reporte.html
└── venv/                   # Entorno virtual (NO subir a Git)

⚙️ Requisitos Previos

Python 3.10 o superior

API REST de Spring Boot ejecutándose

Acceso al endpoint:

http://localhost:8080/api/calificaciones

🧪 Tecnologías Utilizadas
Backend

Spring Boot (API REST)

Hibernate / JPA

MySQL

Análisis de Datos

Python

Pandas

NumPy

Requests

Visualización

Matplotlib

Seaborn

🛠️ Instalación y Configuración
🔹 PASO 1: Crear el Entorno Virtual
python -m venv venv


📌 Esto crea un entorno aislado para las dependencias del proyecto.

🔹 PASO 2: Activar el Entorno Virtual
PowerShell
.\venv\Scripts\Activate.ps1

CMD
venv\Scripts\activate.bat


✔️ Resultado esperado:

(venv) C:\ruta\del\proyecto>

🔹 PASO 3: Instalar Dependencias

Con el entorno virtual activado:

pip install -r requirements.txt

📦 Dependencias Principales

numpy → Cálculos numéricos

pandas → Análisis y manipulación de datos

matplotlib → Gráficos base

seaborn → Visualizaciones estadísticas

requests → Consumo de API REST

⚠️ os NO se instala, es parte de la librería estándar de Python.

🔹 PASO 4: Verificar Instalación (Opcional)
pip list

🔹 PASO 5: Ejecutar el Proyecto

⚠️ Antes de ejecutar Python, asegúrate de que Spring Boot esté corriendo.

Luego ejecuta:

python app.py

✅ Resultado Esperado

Se generan automáticamente los gráficos en la carpeta resultados/

Se crea el archivo:

resultados/reporte.html


En consola se muestran mensajes como:

Valores nulos manejados correctamente.
Texto estandarizado correctamente.


📌 Abre reporte.html en tu navegador para ver el análisis completo.

📊 Análisis y Visualizaciones Generadas
1️⃣ Ranking de Calidad de Platillos

Gráfico de barras

Muestra los platillos mejor valorados

Facilita la identificación de productos estrella

2️⃣ Matriz de Valor: Precio vs Calificación

Gráfico de dispersión

Relaciona precio y satisfacción

Tamaño del punto = cantidad de votos

Permite detectar oportunidades y riesgos comerciales

3️⃣ Fidelidad de Clientes

Gráfico de barras

Muestra los clientes que han probado más variedad de platillos

Útil para estrategias de fidelización

4️⃣ Tabla de Datos Detallados

Tabla HTML interactiva

Permite:

Buscar

Ordenar

Filtrar información

📄 Archivos Clave
Archivo	Descripción
app.py	Orquesta todo el flujo del análisis
data_clean.py	Limpieza, transformación y agregaciones
visualizacion.py	Gráficos estadísticos
estilos.css	Estilos visuales del reporte
reporte.html	Resultado final
📌 Notas Importantes

✅ Activar siempre el entorno virtual
✅ Spring Boot debe estar activo
✅ No se modifican datos en la base de datos
✅ venv/ no debe subirse a GitHub
✅ Proyecto basado en consumo de API REST real

👨‍💻 Autor

Proyecto desarrollado para la asignatura de Análisis de Datos
Integración Python + Spring Boot

Autor: Omar Salcedo, Yhorman Escobar.
Fecha: Enero 2026

🟢 Estado del Proyecto

✔️ Funcional
✔️ Integrado con API REST
✔️ Listo para evaluación académica