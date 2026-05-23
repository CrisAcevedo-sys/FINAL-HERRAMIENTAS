"""
Módulo encargado de cargar el archivo CSV original del DANE
correspondiente a mortalidad en Colombia durante 2019.

Este proceso realiza las siguientes tareas:
1. Carga el archivo original.
2. Selecciona únicamente las columnas necesarias.
3. Renombra las variables para facilitar su interpretación.
4. Guarda un nuevo archivo CSV filtrado para la etapa de transformación.
"""

from pathlib import Path
import pandas as pd


# =========================================================
# RUTAS DE ARCHIVOS
# =========================================================

# Ruta del archivo original suministrado por el DANE
INPUT_CSV: Path = (
    Path(__file__).resolve().parents[1]
    / "0._Datos"
    / "0._Todos_los_datos_2019.csv"
)

# Ruta donde se guardará el archivo filtrado
OUTPUT_CSV: Path = (
    Path(__file__).resolve().parents[1]
    / "0.1._Datos_filtrados_y_transformados"
    / "0.1._Todos_los_datos_2019_filtrado.csv"
)



# Columnas necesarias para el análisis
SELECTED_COLUMNS: list[str] = [
    "COD_DPTO",
    "COD_MUNIC",
    "ANO",
    "MES",
    "SEXO",
    "MUERTEPORO",
    "SIMUERTEPO",
    "CODPTORE",
    "GRU_ED1",
    "CAUSA_MULT",
]

# Renombrado de columnas para mejorar claridad
COLUMN_RENAME: dict[str, str] = {
    "COD_DPTO": "DEPARTAMENTO",
    "COD_MUNIC": "MUNICIPIO",
    "ANO": "AÑO",
    "MES": "MES",
    "SEXO": "SEXO",
    "MUERTEPORO": "MANERA_MUERTE",
    "SIMUERTEPO": "MUERTE_VIOLENTA",
    "CODPTORE": "DPTO_MUERTE_VIOLENTA",
    "GRU_ED1": "GRUPO_EDAD",
}


def main() -> None:
    """
    Carga el archivo original del DANE, filtra las columnas necesarias,
    renombra las variables seleccionadas y guarda el resultado en un nuevo CSV.

    Retorna
    -------
    None
        No retorna ningún valor; solo guarda el archivo filtrado
        y muestra información básica en consola.
    """

    # Cargar el archivo original en un DataFrame
    df: pd.DataFrame = pd.read_csv(
        INPUT_CSV,
        encoding="utf-8",
        low_memory=False
    )

    # Seleccionar únicamente las columnas requeridas para el análisis
    df = df[SELECTED_COLUMNS].copy()

    # Renombrar las columnas para hacerlas más comprensibles
    df.rename(
        columns=COLUMN_RENAME,
        inplace=True
    )

    # Guardar el archivo filtrado en la ruta de salida
    df.to_csv(
        OUTPUT_CSV,
        index=False,
        encoding="utf-8"
    )

    # Mostrar información básica de verificación
    print("Archivo limpio guardado en:", OUTPUT_CSV)
    print("Columnas conservadas:", list(df.columns))
    print("Tamaño del DataFrame:", df.shape)


if __name__ == "__main__":
    main()