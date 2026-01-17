# Restaurante Sabor Urbano - Análisis de Datos

## Descripción del Programa

Esta es una aplicación de análisis de datos en Python que realiza limpieza, preparación y análisis datos extraidos
desde la API REST desarrollada en Spring Boot:

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
   - Limpieza específica (eliminación de símbolos especiales, cálculo de longitud de caracteres)

2. **Script principal (app.py)**:
   - Integración del módulo de limpieza
   - Presentación visual de datos en diferentes etapas del procesamiento
   - Análisis de datos clave:
     - 
     - 
     - 
     - 
3. **Módulo de gráficos (graficos.py)**:
   - Visualización de datos mediante matplotlib y seaborn
   - 
   - 
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

**Resultado esperado**: Verás una salida detallada como:

```
--- Bienvenido a SpringBoot analisis ---
Datos cargados correctamente desde: localhost:8080/api/v1/platillos
--- Vista preliminar de los datos crudos ---
...
```

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

| Acción | Comando |
|--------|---------|
| **Navegar al proyecto** | `cd C:\Users\disenoydesarrollo\Documents\Omar\analisis_datos` |
| **Crear entorno virtual** | `python -m venv venv` |
| **Activar entorno (PowerShell)** | `.\venv\Scripts\Activate.ps1` |
| **Activar entorno (cmd)** | `venv\Scripts\activate.bat` |
| **Instalar dependencias** | `pip install -r requeriments.txt` |
| **Ejecutar el programa** | `python app.py` |
| **Desactivar entorno** | `deactivate` |
| **Ver paquetes instalados** | `pip list` |

---

## Flujo de Ejecución del Programa


## Archivos del Proyecto

- **app.py**: Script principal que orquesta el flujo del programa
- **data_clean.py**: Módulo con funciones de limpieza y procesamiento de datos


---


## Notas Importantes

✅ **Siempre activa el entorno virtual antes de ejecutar el programa**
✅ **El archivo `requeriments.txt` asegura que todos tengan las mismas versiones**
✅ **Los datos se procesan en memoria (el programa no modifica los CSV originales)**
✅ **La carpeta `venv` no debe subirse a GitHub (se incluye en .gitignore)**

---

## Autor

Proyecto desarrollado como parte del análisis de datos en Python.

---

**Última actualización**: Enero 2026
