"""
Módulo encargado de transformar los datos filtrados de mortalidad
en Colombia correspondientes al año 2019.

Este proceso realiza:
1. Conversión de variables numéricas a texto.
2. Clasificación de grupos de edad.
3. Creación del código DIVIPOLA.
4. Asociación de municipios mediante diccionario de ciudades.
5. Generación de un nuevo archivo CSV listo para análisis y visualización.
"""

from pathlib import Path
import pandas as pd
import sys

# Agregar directorio raíz al PATH del proyecto
ROOT_DIR: Path = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

# Importar diccionario de municipios
from diccionarios.ciudades import CIUDADES_MAP



# RUTAS


# Ruta del archivo previamente filtrado
INPUT_CSV: Path = (
    Path(__file__).resolve().parents[1]
    / "0.1._Datos_filtrados_y_transformados"
    / "0.1._Todos_los_datos_2019_transformado.csv"
)

# Ruta donde se guardará el archivo transformado
OUTPUT_CSV: Path = (
    Path(__file__).resolve().parents[1]
    / "0.1._Datos_filtrados_y_transformados"
    / "0.1._Todos_los_datos_2019_transformado.csv"
)



# DICCIONARIOS DE TRANSFORMACIÓN


DEPARTAMENTO_MAP: dict[int, str] = {
    5: "Antioquia",
    8: "Atlántico",
    11: "Bogotá",
    13: "Bolívar",
    15: "Boyacá",
    17: "Caldas",
    18: "Caquetá",
    19: "Cauca",
    20: "Cesar",
    23: "Córdoba",
    25: "Cundinamarca",
    27: "Chocó",
    41: "Huila",
    44: "La Guajira",
    47: "Magdalena",
    50: "Meta",
    52: "Nariño",
    54: "Norte de Santander",
    63: "Quindío",
    66: "Risaralda",
    68: "Santander",
    70: "Sucre",
    73: "Tolima",
    76: "Valle del Cauca",
    81: "Arauca",
    85: "Casanare",
    86: "Putumayo",
    88: "San Andrés",
    91: "Amazonas",
    94: "Guainía",
    95: "Guaviare",
    97: "Vaupés",
    99: "Vichada",
}

MES_MAP: dict[int, str] = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

MANERA_MUERTE_MAP: dict[int, str] = {
    0: "Natural (Enfermedad)",
    1: "Homicidio",
    2: "Accidente",
    3: "Pendiente de investigación",
    4: "Suicidio",
    5: "No determinada",
    6: "Desconocida",
    8: "Intervención legal",
    9: "Guerra",
}

MUERTE_VIOLENTA_MAP: dict[int, str] = {
    1: "Sí",
    2: "No",
    9: "Sin información",
}

DPTO_MUERTE_VIOLENTA_MAP: dict[int, str] = {
    1: "Sin información",
    **DEPARTAMENTO_MAP,
}

SEXO_MAP: dict[int, str] = {
    1: "Masculino",
    2: "Femenino",
    3: "Indeterminado",
}



# FUNCIONES AUXILIARES


def apply_mapping(
    series: pd.Series,
    mapping: dict
) -> pd.Series:
    """
    Convierte valores numéricos a texto usando un diccionario.

    Parámetros
    ----------
    series : pd.Series
        Serie con datos numéricos.

    mapping : dict
        Diccionario de equivalencias.

    Retorna
    -------
    pd.Series
        Serie transformada a texto.
    """

    mapped: pd.Series = series.map(mapping)

    return mapped.fillna("Sin información")


def clasificar_edad(valor: int) -> str:
    """
    Clasifica un código de grupo de edad según categorías DANE.

    Parámetros
    ----------
    valor : int
        Código numérico del grupo de edad.

    Retorna
    -------
    str
        Categoría de edad correspondiente.
    """

    if pd.isna(valor):
        return "Sin información"

    valor = int(valor)

    if 0 <= valor <= 4:
        return "Mortalidad neonatal"

    elif 5 <= valor <= 6:
        return "Mortalidad infantil"

    elif 7 <= valor <= 8:
        return "Primera infancia"

    elif 9 <= valor <= 10:
        return "Niñez"

    elif valor == 11:
        return "Adolescencia"

    elif 12 <= valor <= 13:
        return "Juventud"

    elif 14 <= valor <= 16:
        return "Adultez temprana"

    elif 17 <= valor <= 19:
        return "Adultez intermedia"

    elif 20 <= valor <= 24:
        return "Vejez"

    elif 25 <= valor <= 28:
        return "Longevidad / Centenarios"

    elif valor == 29:
        return "Edad desconocida"

    return "Sin información"



# CREACIÓN DE CÓDIGO DIVIPOLA


def crear_divipola(df: pd.DataFrame) -> pd.Series:
    """
    Genera el código DIVIPOLA uniendo departamento y municipio.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame principal.

    Retorna
    -------
    pd.Series
        Serie con códigos DIVIPOLA.
    """

    depto: pd.Series = (
        pd.to_numeric(
            df["DEPARTAMENTO"],
            errors="coerce"
        )
        .fillna(0)
        .astype(int)
        .astype(str)
        .str.zfill(2)
    )

    municipio: pd.Series = (
        pd.to_numeric(
            df["COD_MUNIC"],
            errors="coerce"
        )
        .fillna(0)
        .astype(int)
        .astype(str)
        .str.zfill(3)
    )

    return depto + municipio



# FUNCIÓN PRINCIPAL


def main() -> None:
    """
    Ejecuta el proceso completo de transformación de datos.

    Retorna
    -------
    None
    """

    # Cargar archivo filtrado
    df: pd.DataFrame = pd.read_csv(
        INPUT_CSV,
        encoding="utf-8"
    )

    print("Columnas originales:")
    print(df.columns.tolist())

   
    # TRANSFORMACIÓN DE VARIABLES A TEXTO
    

    df["DEPARTAMENTO_TEXTO"] = apply_mapping(
        df["DEPARTAMENTO"].astype("Int64"),
        DEPARTAMENTO_MAP
    )

    df["MES_TEXTO"] = apply_mapping(
        df["MES"].astype("Int64"),
        MES_MAP
    )

    df["MANERA_MUERTE_TEXTO"] = apply_mapping(
        df["MANERA_MUERTE"].astype("Int64"),
        MANERA_MUERTE_MAP
    )

    df["MUERTE_VIOLENTA_TEXTO"] = apply_mapping(
        df["MUERTE_VIOLENTA"].astype("Int64"),
        MUERTE_VIOLENTA_MAP
    )

    df["DPTO_MUERTE_VIOLENTA_TEXTO"] = apply_mapping(
        df["DPTO_MUERTE_VIOLENTA"].astype("Int64"),
        DPTO_MUERTE_VIOLENTA_MAP
    )

    df["SEXO_TEXTO"] = apply_mapping(
        df["SEXO"].astype("Int64"),
        SEXO_MAP
    )

    
    # CLASIFICACIÓN DE EDADES
    

    df["GRUPO_EDAD_TEXTO"] = (
        df["GRUPO_EDAD"]
        .apply(clasificar_edad)
    )

    
    # CREAR DIVIPOLA
    

    df["DIVIPOLA"] = crear_divipola(df)

    
    # ASIGNAR NOMBRE DE MUNICIPIOS
   

    df["CIUDAD_TEXTO"] = (
        df["DIVIPOLA"]
        .map(CIUDADES_MAP)
    )

    df["CIUDAD_TEXTO"] = (
        df["CIUDAD_TEXTO"]
        .fillna("Municipio desconocido")
    )

    # CREAR CARPETA DE SALIDA
    

    OUTPUT_CSV.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    
    # GUARDAR ARCHIVO TRANSFORMADO
   

    df.to_csv(
        OUTPUT_CSV,
        index=False,
        encoding="utf-8"
    )

    print("\nArchivo transformado guardado correctamente.")
    print("\nColumnas finales:")
    print(df.columns.tolist())


if __name__ == "__main__":
    main()