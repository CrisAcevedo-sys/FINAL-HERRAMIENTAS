import streamlit as st
import pandas as pd

from diccionarios.icd10 import ICD10_MAP


def tabla_principales_causas(df: pd.DataFrame) -> None:
    """
    Muestra una tabla con las principales causas de muerte
    basadas en códigos ICD-10.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con datos de mortalidad.

    Retorna
    -------
    None
    """

    # Copia del DataFrame
    datos = df.copy()

    # Normalizar códigos ICD-10
    datos["CAUSA_MULT"] = (
        datos["CAUSA_MULT"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # Agrupar por causa
    causas = (
        datos.groupby("CAUSA_MULT")
        .size()
        .reset_index(name="TOTAL_CASOS")
    )

    # Filtrar códigos válidos
    causas = causas[causas["CAUSA_MULT"].isin(ICD10_MAP.keys())]

    # Mapear nombre de causa
    causas["NOMBRE_CAUSA"] = causas["CAUSA_MULT"].map(ICD10_MAP)

    # Ordenar top 10
    causas = (
        causas.sort_values(by="TOTAL_CASOS", ascending=False)
        .head(10)
    )

    # Renombrar columnas
    causas = causas.rename(
        columns={
            "CAUSA_MULT": "Código ICD-10",
            "NOMBRE_CAUSA": "Causa de muerte",
            "TOTAL_CASOS": "Total casos"
        }
    )

    
    # TÍTULO
    
    st.subheader("10 principales causas de muerte en Colombia")

    
    st.dataframe(
        causas,
        use_container_width=True,
        hide_index=True
    )

    # INTERPRETACIÓN
    
    if not causas.empty:

        principal = causas.iloc[0]

        st.info(
            f"La principal causa de muerte fue "
            f"**{principal['Causa de muerte']}** con "
            f"**{principal['Total casos']:,} casos**."
        )