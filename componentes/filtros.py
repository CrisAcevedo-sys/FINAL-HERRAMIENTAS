import streamlit as st
import pandas as pd


def aplicar_filtros(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Aplica filtros interactivos sobre el DataFrame principal
    utilizando la barra lateral de Streamlit.

    Los filtros permiten seleccionar:
    - departamento,
    - ciudad o municipio,
    - sexo,
    - mes.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame principal con los datos de mortalidad.

    Retorna
    -------
    pd.DataFrame
        DataFrame filtrado según las selecciones del usuario.
    """

    # Título de la barra lateral
    st.sidebar.header("Filtros")

    # Filtro de departamentos
    departamentos: list[str] = st.sidebar.multiselect(
        "Departamento",
        options=sorted(
            df["DEPARTAMENTO_TEXTO"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["DEPARTAMENTO_TEXTO"]
            .dropna()
            .unique()
        ),
    )

    # Filtrar temporalmente por departamento
    df_depto: pd.DataFrame = df[
        df["DEPARTAMENTO_TEXTO"]
        .isin(departamentos)
    ]

    # Filtro de ciudades o municipios
    ciudades: list[str] = st.sidebar.multiselect(
        "Ciudad / municipio",
        options=sorted(
            df_depto["CIUDAD_TEXTO"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df_depto["CIUDAD_TEXTO"]
            .dropna()
            .unique()
        ),
    )

    # Filtro de sexo
    sexo: list[str] = st.sidebar.multiselect(
        "Sexo",
        options=sorted(
            df["SEXO_TEXTO"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["SEXO_TEXTO"]
            .dropna()
            .unique()
        ),
    )

    # Filtro de meses
    meses: list[str] = st.sidebar.multiselect(
        "Mes",
        options=sorted(
            df["MES_TEXTO"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["MES_TEXTO"]
            .dropna()
            .unique()
        ),
    )

    # Aplicar todos los filtros seleccionados
    df_filtrado: pd.DataFrame = df[
        df["DEPARTAMENTO_TEXTO"].isin(departamentos)
        & df["CIUDAD_TEXTO"].isin(ciudades)
        & df["SEXO_TEXTO"].isin(sexo)
        & df["MES_TEXTO"].isin(meses)
    ]

    return df_filtrado