import streamlit as st
import pandas as pd


def mostrar_kpis(
    df: pd.DataFrame
) -> None:
    """
    Muestra indicadores principales de mortalidad
    utilizando métricas visuales en Streamlit.

    Los KPIs permiten identificar:
    - total de muertes,
    - cantidad de departamentos,
    - cantidad de municipios,
    - departamento con más muertes,
    - ciudad con más muertes,
    - porcentaje de homicidios.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame principal con los datos de mortalidad.

    Retorna
    -------
    None
        No retorna valores; únicamente renderiza
        componentes visuales en Streamlit.
    """

    # Crear copia para evitar modificar el DataFrame original
    datos: pd.DataFrame = df.copy()

    # Convertir DIVIPOLA a texto
    # DIVIPOLA es el código oficial utilizado por el DANE
    # para identificar departamentos y municipios en Colombia.
    # Se construye uniendo:
    # - código del departamento
    # - código del municipio
    #
    # Ejemplo:
    # 05 + 001 = 05001 (Medellín)
    datos["DIVIPOLA"] = (
        datos["DIVIPOLA"]
        .astype(str)
        .str.strip()
    )

    # Limpiar espacios innecesarios en nombres de ciudades
    datos["CIUDAD_TEXTO"] = (
        datos["CIUDAD_TEXTO"]
        .astype(str)
        .str.strip()
    )

    # Calcular total general de registros de mortalidad
    total_muertes: int = len(datos)

    # Calcular cantidad de departamentos únicos
    total_departamentos: int = (
        datos["DEPARTAMENTO_TEXTO"]
        .dropna()
        .nunique()
    )

    # Calcular cantidad de municipios únicos
    # Se utiliza DIVIPOLA porque es más preciso
    # que usar únicamente nombres de ciudades.
    total_municipios: int = (
        datos["DIVIPOLA"]
        .nunique()
    )

    # Agrupar muertes por departamento
    deptos: pd.DataFrame = (
        datos.groupby("DEPARTAMENTO_TEXTO")
        .size()
        .reset_index(name="TOTAL")
        .sort_values(
            by="TOTAL",
            ascending=False
        )
    )

    # Obtener el departamento con más casos
    depto_top: pd.Series = deptos.iloc[0]

    # Crear copia para trabajar únicamente
    # con municipios válidos
    ciudades: pd.DataFrame = datos.copy()

    # Eliminar municipios vacíos
    ciudades = ciudades[
        ciudades["DIVIPOLA"].notna()
    ]

    # Eliminar registros sin nombre reconocido
    ciudades = ciudades[
        ~ciudades["CIUDAD_TEXTO"]
        .str.contains(
            "desconocido",
            case=False,
            na=False
        )
    ]

    # Agrupar muertes por ciudad
    ciudades_top: pd.DataFrame = (
        ciudades.groupby("CIUDAD_TEXTO")
        .size()
        .reset_index(name="TOTAL")
        .sort_values(
            by="TOTAL",
            ascending=False
        )
    )

    # Obtener ciudad con más muertes
    ciudad_top: pd.Series = ciudades_top.iloc[0]

    # Filtrar homicidios según códigos ICD-10
    #
    # ICD-10:
    # Sistema internacional de clasificación de enfermedades
    # utilizado por la OMS.
    #
    # X95, X96 y X97 corresponden a:
    # agresiones con armas de fuego.
    homicidios: pd.DataFrame = datos[
        datos["CAUSA_MULT"]
        .astype(str)
        .str.upper()
        .str.startswith(
            ("X95", "X96", "X97"),
            na=False
        )
    ]

    # Total de homicidios encontrados
    total_homicidios: int = len(homicidios)

    # Calcular porcentaje de homicidios
    porcentaje_homicidios: float = (
        total_homicidios / total_muertes
    ) * 100

    # Estilos CSS personalizados para métricas
    st.markdown(
        """
        <style>

        div[data-testid="metric-container"]{
            background: linear-gradient(
                135deg,
                #111827,
                #1f2937
            );

            border-radius:18px;

            padding:22px;

            border:1px solid #374151;

            box-shadow:
            0px 4px 18px
            rgba(0,0,0,0.30);
        }

        div[data-testid="metric-container"] label{
            font-weight:700;
            font-size:15px;
        }

        div[data-testid="metric-container"] div{
            color:white;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Título de la sección
    st.subheader(
        "Indicadores principales de mortalidad"
    )

    # Crear primera fila de KPIs
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total muertes",
        f"{total_muertes:,}"
    )

    col2.metric(
        "Departamentos",
        total_departamentos
    )

    col3.metric(
        "Municipios",
        total_municipios
    )

    # Crear segunda fila de KPIs
    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Departamento más afectado",
        depto_top["DEPARTAMENTO_TEXTO"],
        f"{depto_top['TOTAL']:,} casos"
    )

    col5.metric(
        "Ciudad más afectada",
        ciudad_top["CIUDAD_TEXTO"],
        f"{ciudad_top['TOTAL']:,} casos"
    )

    col6.metric(
        "Homicidios",
        f"{porcentaje_homicidios:.2f}%",
        f"{total_homicidios:,} casos"
    )