"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    # 1. Cargar el archivo (ajusta la ruta si es necesario)
    df = pd.read_csv("files/input/keywords.csv")

    # 2. Agrupar por 'cluster'
    # 'cantidad_de_palabras_clave' es el conteo por grupo
    df_grouped = df.groupby("cluster")["keyword"].agg(
        cantidad_de_palabras_clave="count",
        principales_palabras_clave=lambda x: ", ".join(sorted(x))
    )

    # 3. Calcular el porcentaje
    total_keywords = df_grouped["cantidad_de_palabras_clave"].sum()
    df_grouped["porcentaje_de_palabras_clave"] = (
        (df_grouped["cantidad_de_palabras_clave"] / total_keywords) * 100
    ).round(1)

    # 4. Formatear y ordenar
    df_grouped = df_grouped.reset_index()
    
    # Asegurar que las columnas estén en el orden correcto
    return df_grouped[[
        "cluster", 
        "cantidad_de_palabras_clave", 
        "porcentaje_de_palabras_clave", 
        "principales_palabras_clave"
    ]]

    
