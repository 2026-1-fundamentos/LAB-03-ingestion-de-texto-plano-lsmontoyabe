"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import re 
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
    with open("files/input/clusters_report.txt", encoding="utf-8") as f:
        lines = f.readlines()

    registros = []
    actual = None

    for line in lines:

        # elimina salto de línea
        line = line.rstrip()

        # inicio de un nuevo cluster
        m = re.match(
            r"^\s*(\d+)\s+(\d+)\s+(\d+,\d+)\s+%\s+(.*)$",
            line,
        )

        if m:

            if actual is not None:
                registros.append(actual)

            actual = {
                "cluster": int(m.group(1)),
                "cantidad_de_palabras_clave": int(m.group(2)),
                "porcentaje_de_palabras_clave": float(
                    m.group(3).replace(",", ".")
                ),
                "principales_palabras_clave": m.group(4).strip(),
            }

        elif actual is not None:

            texto = line.strip()

            if texto != "":
                actual["principales_palabras_clave"] += " " + texto

    registros.append(actual)

    df = pd.DataFrame(registros)

    # eliminar múltiples espacios
    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)
        .str.replace(r"\s*,\s*", ", ", regex=True)
        .str.replace(r"\.$", "", regex=True)
        .str.strip()
    )

    return df