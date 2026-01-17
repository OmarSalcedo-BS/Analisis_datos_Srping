# Restaurante Sabor Urbano - Análisis de Datos

## Descripción del Programa

Esta es una aplicación de análisis de datos en Python que realiza limpieza, preparación y análisis datos extraidos
desde la API REST desarrollada en Spring Boot por lo que esta funciona en conjunto y debe ser inciada:

- **Cargar datos** Desde los endpoints de la API REST
- **Limpiar y estandarizar datos** (manejo de valores nulos, normalización de texto)
- **Realizar análisis estadísticos** mediante operaciones de filtrado y comparaciones
- **Generar Graficos con datos procesados** Con esto se podran realizar comparativas de platos
  populares, comentarios y calificaciones

### Características Principales:

1. **Módulo de limpieza (data_clean.py)**:
   - Carga de datos desde endpoints de la API REST
   - Manejo de valores nulos (eliminación de filas críticas, relleno de valores faltantes)
   - Estandarización de texto (conversión a minúsculas, eliminación de espacios extra)
   - Extracción de datos de fidelidad de clientes
   - Preparación de DataFrames agregados para análisis específicos

2. **Script principal (app.py)**:
   - Integración del módulo de limpieza y visualización
   - Generación automática de un reporte HTML interactivo (`reporte.html`)
   - Orquestación del flujo de datos: Carga -> Limpieza -> Análisis -> Visualización

3. **Módulo de gráficos (visualizacion.py)**:
   - Generación de gráficos estadísticos con **Seaborn** y **Matplotlib**:
     - **Ranking de Calidad**: Gráfico de barras de los platillos mejor valorados.
     - **Matriz de Valor**: Gráfico de dispersión (Scatter Plot) relacionando Precio vs Calidad.
     - **Fidelidad de Clientes**: Análisis de los clientes que han probado más variedad de platillos.

4. **Estilos y Presentación (estilos.css)**:
   - Hoja de estilos moderna para el reporte HTML, asegurando una presentación profesional y limpia de los datos.

---

## Paso a Paso: Instalación y Configuración

### **PASO 1: Crear el Entorno Virtual**

Un entorno virtual es un espacio aislado donde se instalan las dependencias del proyecto sin afectar el Python global.

#### Crear el entorno:

```powershell
python -m venv venv
```

**¿Qué hace este comando?**

- `-m venv`: Usa el módulo venv de Python
- `venv`: Crea una carpeta llamada "venv" con el entorno virtual

**Resultado esperado**: Se crea una carpeta `venv` en tu proyecto (esto puede tardar 10-30 segundos)

---

### **PASO 2: Activar el Entorno Virtual**

#### En PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

#### En Símbolo del Sistema (cmd):

```cmd
venv\Scripts\activate.bat
```

**¿Qué hace este comando?**

- Activa el entorno virtual aislado
- Los paquetes instalados solo afectarán este entorno

**Resultado esperado**: Tu línea de comando debe mostrar `(venv)` al inicio:

```powershell
(venv) C:\Users\disenoydesarrollo\Documents\Omar\analisis_datos>
```

---

### **PASO 3: Instalar las Dependencias**

Con el entorno virtual activado, instala todos los paquetes requeridos:

```powershell
pip install -r requeriments.txt
```

**¿Qué hace este comando?**

- Lee el archivo `requeriments.txt`
- Instala las versiones específicas de cada paquete necesario:
  - **numpy**: Procesamiento numérico
  - **pandas**: Análisis y manipulación de datos
  - **python-dateutil**: Manejo de fechas
  - **pytz**: Información de zonas horarias
  - **six**: Compatibilidad Python 2/3
  - **tzdata**: Datos de zonas horarias
  - **Seaborn**: Generación de gráficos
  - **matplotlib**: Generación de gráficos
  - **os**: Manejo de archivos y carpetas
  - **requests**: Hacer peticiones HTTP

**Resultado esperado**: Mensaje similar a "Successfully installed..."

```powershell
Collecting numpy==2.3.5
Downloading numpy-2.3.5-cp312-cp312-win_amd64.whl...
...
Successfully installed numpy-2.3.5 pandas-2.3.3 ...
```

---

### **PASO 4: Verificar la Instalación (Opcional)**

Para asegurar que todo se instaló correctamente:

```powershell
pip list
```

**Resultado esperado**: Debes ver los paquetes instalados listados:

```
Package            Version
------------------ ---------
numpy              2.3.5
pandas             2.3.3
python-dateutil    2.9.0.post0
pytz               2025.2
seaborn            0.13.2
matplotlib         3.10.8
os                 0.1.0
requests           2.32.3
**Otros paquetes que se instalan con pandas**
...
```

---

### **PASO 5: Ejecutar el Programa**

Con el entorno virtual activado y las dependencias instaladas:

```powershell
python app.py
```

**¿Qué hace este comando?**

- Ejecuta el script principal `app.py`
- Carga los datos desde los archivos CSV
- Realiza todas las transformaciones y análisis
- Muestra los resultados en la consola

**Resultado esperado**:

- Se generarán las imágenes de los gráficos en la carpeta `resultados/`.
- Se creará un archivo `reporte.html` en la raíz del proyecto.
- Mensajes de confirmación en la consola:

```
Valores nulos manejados correctamente.
Texto estandarizado y precios formateados.
```

- **¡Importante!**: Abre el archivo `reporte.html` en tu navegador para ver el análisis completo.

---

## Desactivar el Entorno Virtual

Cuando termines de trabajar, desactiva el entorno virtual:

```powershell
deactivate
```

**Resultado esperado**: Desaparece `(venv)` del inicio de tu línea de comando:

```powershell
C:\Users\disenoydesarrollo\Documents\Omar\analisis_datos>
```

---

## Resumen de Comandos

| Acción                           | Comando                                                       |
| -------------------------------- | ------------------------------------------------------------- |
| **Navegar al proyecto**          | `cd C:\Users\disenoydesarrollo\Documents\Omar\analisis_datos` |
| **Crear entorno virtual**        | `python -m venv venv`                                         |
| **Activar entorno (PowerShell)** | `.\venv\Scripts\Activate.ps1`                                 |
| **Activar entorno (cmd)**        | `venv\Scripts\activate.bat`                                   |
| **Instalar dependencias**        | `pip install -r requeriments.txt`                             |
| **Ejecutar el programa**         | `python app.py`                                               |
| **Desactivar entorno**           | `deactivate`                                                  |
| **Ver paquetes instalados**      | `pip list`                                                    |

---

## Resultados y Análisis Visual

El programa genera un reporte visual (`reporte.html`) que incluye:

### 1. Ranking de Calidad (Ranking de Calidad)

**Visualización**: Gráfico de barras horizontal.
**Hallazgo**: Permite identificar rápidamente cuáles son los platillos "estrella" del menú (puntuaciones cercanas a 5.0) y cuáles necesitan mejoras.

### 2. Matriz de Valor (Precio vs Calidad)

**Visualización**: Gráfico de dispersión (Scatter Plot).
**Hallazgo**:

- Muestra la relación entre el costo del platillo y la satisfacción del cliente.
- Ayuda a detectar platillos caros con baja calificación (riesgo) o platillos económicos con alta calificación (oportunidad de valor).
- El tamaño de las burbujas indica la **popularidad** (total de votos).

### 3. Fidelidad de Clientes (Clientes Frecuentes)

**Visualización**: Gráfico de barras.
**Hallazgo**: Destaca a los clientes que han probado una mayor variedad de platillos, útil para programas de fidelización.

### 4. Tabla de Datos Detallada

**Visualización**: Tabla interactiva (DataTables).
**Funcionalidad**: Permite buscar, filtrar y ordenar los datos crudos procesados directamente desde el navegador.

---

## Archivos del Proyecto

- **app.py**: Script principal que orquesta la ejecución, genera las rutas y construye el HTML.
- **data_clean.py**: Lógica de negocio para limpieza, transformación y agregación de datos.
- **visualizacion.py**: Librería personalizada para la generación de gráficos con Seaborn.
- **estilos.css**: Definiciones de diseño para el reporte final.
- **reporte.html**: (Generado) El producto final visualizable por el usuario.

---

## Notas Importantes

✅ **Siempre activa el entorno virtual antes de ejecutar el programa**
✅ **El archivo `requeriments.txt` asegura que todos tengan las mismas versiones**
✅ **Los datos se procesan en memoria (el programa no modifica los CSV originales)**
✅ **La carpeta `venv` no debe subirse a GitHub (se incluye en .gitignore)**
✅ **El archivo `reporte.html` se genera en la carpeta `resultados`**
✅ **Este proyecto funciona con una API REST desarrollada en Spring Boot Que se debe iniciar previamente**

---

## Autor

Proyecto desarrollado como parte del análisis de datos en Python.
Omar salcedo

---

**Última actualización**: Enero 2026
