# 🧠 SentimentAPI — Data Science MVP

> **Hackathon ONE | Equipo Data Science**

### 📌 Contexto del Proyecto: SentimentAPI

Este repositorio es un **espejo de mi contribución individual** al proyecto `SentimentAPI`, desarrollado en el marco de un **hackathon** por un equipo de  **8 personas** .

`SentimentAPI` es un **microservicio inteligente** que expone una API REST capaz de recibir feedback de usuarios (reseñas, comentarios, encuestas, etc.) y devolver una **predicción de sentimiento** (positivo, negativo, neutral) en tiempo real. El objetivo del proyecto era construir una solución completa, desde la ingesta de datos hasta el despliegue del modelo.

### 🧩 Mi rol en el equipo

Dentro del equipo fui responsable de la **fase de preparación y limpieza de datos** (Data Engineering + Data Science). Este notebook contiene  **mi parte exclusiva del trabajo** :

* **Procesamiento de 3 datasets heterogéneos** (diferentes formatos, codificaciones y niveles de granularidad).
* **Pipeline de limpieza, normalización y categorización** de sentimientos en español.
* **Generación de un dataset unificado y balanceado** , listo para entrenar el modelo de clasificación que usaría el microservicio.

> ⚠️  **Nota importante** : Este repositorio **no incluye** el código del microservicio (API, despliegue, etc.) ni el trabajo del resto del equipo. Es únicamente una muestra de mis capacidades como especialista en procesamiento de datos y documentación técnica, pensado para que reclutadores y aprendices puedan evaluar mi enfoque, calidad de código y toma de decisiones.

---

### Enlaces del Proyecto

[Proyecto Proyecto 1: SentimentAPI — Análisis de Sentimientos de Feedbacks para Data Science | No Country | No Country](https://nocountry.tech/hackathon-one-ii-latam/cmj15mkcy001joy014aszb3z5)

[Repositorio GitHub Sentiment API (original)](https://github.com/ml-punto-tech/sentiment-api)

---

### 🧠 Pipeline de Análisis de Sentimientos

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![Hackathon](https://img.shields.io/badge/Hackathon-SentimentAPI-green)](https://github.com/tu-usuario/SentimentAPI-refactor)

> **Notebook**: `Modelo_SentimentAPI.ipynb`
> **Autor**: [Marely Cárcamo Quisto](https://www.linkedin.com/in/marely/)
> **Propósito**: Procesar, limpiar y unificar múltiples datasets de sentimientos en español, transformándolos en un dataset de alta calidad listo para modelos de Machine Learning.

### 📌 Descripción Notebook SentimentAPI

Este notebook implementa un **pipeline de datos completo** para análisis de sentimientos en español.
Toma **tres datasets crudos** con diferentes estructuras, codificaciones y niveles de granularidad, y los convierte en un único conjunto de datos **balanceado, sin contradicciones y con sentimientos normalizados** (positivo / negativo / neutral).

El pipeline está diseñado para ser **escalable**, **modular** y **reproducible** – añadir un nuevo dataset solo requiere una línea en un diccionario de configuración.



---


🔧 Detalles técnicos destacados de mi implementación
A continuación se describen las decisiones de diseño y las técnicas implementadas en el notebook, pensadas para garantizar trazabilidad, escalabilidad y calidad del dato.

#### 1. Arquitectura modular y escalable con procesar_dic()
Creé una función genérica procesar_dic() que aplica cualquier función de transformación a todos los DataFrames almacenados en un diccionario.

Esto permite añadir nuevos datasets simplemente agregando una entrada al diccionario datasets, sin modificar el resto del pipeline.

Cada etapa (carga, filtrado, limpieza) genera un nuevo diccionario con sufijos consistentes (_cargado, _filtrado, _limpio), evitando inconsistencias y sobrescrituras accidentales.

#### 2. Trazabilidad total mediante acumuladores y variables globales
Implementé un sistema de contadores acumulativos (CONTADOR_GLOBAL) que registra, paso a paso, el número de registros eliminados por:

Contradicciones semánticas (mismo texto con distinto sentimiento)

Duplicados exactos (mismo texto + mismo sentimiento)

Valores nulos o vacíos

Estos acumuladores se actualizan en cada fase y al final alimentan un gráfico interactivo (Plotly) que muestra de forma visual el impacto de cada criterio de limpieza.

La lógica está encapsulada en la función limpieza_dataframe_unificado(), que además adjunta las estadísticas como atributo del DataFrame (df.estadisticas_limpieza), facilitando su reutilización y auditoría.

#### 3. Clasificación inteligente con diccionario externo
Los datasets originales tenían una granularidad excesiva: hasta 105 sentimientos distintos (ej. "admiración", "asombro", "adoración").

Para reducir la dimensionalidad y facilitar el aprendizaje supervisado, cargué un diccionario externo de 106 términos (descargado desde GitHub) que mapea cada sentimiento específico a una de tres categorías: positivo, negativo o neutral.

La función categorizar_sentimiento() aplica este mapeo de forma eficiente y tolerante a mayúsculas/minúsculas.

#### 4. Limpieza de texto robusta para el español
La función limpiar_texto_sentimientos() realiza una normalización Unicode (NFD) para eliminar tildes, pero preserva la letra ñ mediante un sistema de marcadores temporales – algo crítico en español para no perder significado ("año" ≠ "ano").

También se eliminan hashtags, URLs rotas, caracteres no imprimibles y se normalizan espacios múltiples.

Se mantiene la mayúsculas iniciales para no perder posibles señales emocionales (ej. "FELIZ" vs "feliz").

#### 5. Detección automática de encoding y manejo de errores de red
Cada dataset se descarga desde una URL pública. La función importar_dataset() utiliza chardet para detectar automáticamente el encoding (UTF-8, Windows-1252, ISO-8859-15, etc.), evitando caracteres corruptos.

Incluye reintentos con separadores alternativos (, , ; , \t) si el especificado falla.

Captura excepciones HTTPError y URLError para informar fallos sin detener todo el pipeline.

#### 6. Eliminación de contradicciones semánticas (decisión fundamentada)
Detecté que algunos textos aparecían etiquetados con diferentes sentimientos en distintos registros (ej. la misma frase marcada como positivo y negativo).

Decisión: eliminé todos los registros de esos textos contradictorios (216 casos), porque entrenar con ellos introduciría ruido insalvable.
Justificación documentada en el notebook.

#### 7. Visualización interactiva para comunicación de resultados
Utilicé plotly.graph_objects y make_subplots para generar un dashboard de dos paneles:

Barras horizontales que desglosan las causas de eliminación.

Gráfico circular que muestra la proporción final de registros conservados vs. eliminados.

La distribución final de sentimientos se presenta también con un gráfico combinado (pie + barras), evidenciando el balance logrado (≈34% cada clase).

💡 Estas decisiones reflejan mi enfoque en código mantenible, auditoría de datos, escalabilidad y comunicación visual de resultados – cualidades que considero fundamentales en entornos colaborativos y de producción.

⚠️ Nota importante
Este repositorio no incluye el código del microservicio (API, despliegue, etc.) ni el trabajo del resto del equipo. Es únicamente una muestra de mis capacidades como especialista en procesamiento de datos y documentación técnica, pensado para que reclutadores y aprendices puedan evaluar mi enfoque, calidad de código y toma de decisiones.

Si quieres, puedo añadir un diagrama de flujo (en texto o con emojis) resumiendo el pipeline, o crear una tabla con los resultados numéricos finales. Dime si prefieres alguna variación.

