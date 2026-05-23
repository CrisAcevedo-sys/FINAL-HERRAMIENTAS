import streamlit as st
import pandas as pd


def interpretar_patrones(df: pd.DataFrame) -> None:
    """
    Genera un análisis descriptivo de patrones de mortalidad
    basado en agregaciones por variables categóricas.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con datos de mortalidad.

    Retorna
    -------
    None
    """

    st.header("Interpretación de patrones de mortalidad")

    
    # TERRITORIO
   

    # Agrupar por departamento
    deptos = (
        df.groupby("DEPARTAMENTO_TEXTO")
        .size()
        .sort_values(ascending=False)
    )

    depto_max: str = deptos.idxmax()
    depto_total: int = int(deptos.max())

    st.subheader("Patrón territorial")

    st.write(
        f"""
        El departamento con mayor cantidad de
        muertes registradas en 2019 fue
        **{depto_max}** con un total de
        **{depto_total:,} casos**.
        """
    )

  
    # MES
    

    # Agrupar por mes
    meses = (
        df.groupby("MES_TEXTO")
        .size()
        .sort_values(ascending=False)
    )

    mes_max: str = meses.idxmax()
    total_mes: int = int(meses.max())

    st.subheader("Patrón temporal")

    st.write(
        f"""
        El mes con mayor número de muertes fue
        **{mes_max}** con
        **{total_mes:,} registros**.
        """
    )

    
    # SEXO
   

    # Agrupar por sexo
    sexo = (
        df.groupby("SEXO_TEXTO")
        .size()
        .sort_values(ascending=False)
    )

    sexo_max: str = sexo.idxmax()
    total_sexo: int = int(sexo.max())

    st.subheader("Patrón por sexo")

    st.write(
        f"""
        El sexo con mayor cantidad de muertes fue
        **{sexo_max}** con
        **{total_sexo:,} casos**.
        """
    )

    # EDAD
  

    # Agrupar por grupo de edad
    edad = (
        df.groupby("GRUPO_EDAD_TEXTO")
        .size()
        .sort_values(ascending=False)
    )

    edad_max: str = edad.idxmax()
    total_edad: int = int(edad.max())

    st.subheader("Patrón por grupo de edad")

    st.write(
        f"""
        El grupo de edad más afectado fue
        **{edad_max}** con
        **{total_edad:,} muertes**.
        """
    )

   
    # CAUSAS
  

    # Agrupar por causa de muerte
    causas = (
        df.groupby("CAUSA_MULT")
        .size()
        .sort_values(ascending=False)
    )

    causa_max: str = causas.idxmax()
    total_causa: int = int(causas.max())

    st.subheader("Patrón por causa de muerte")

    st.write(
        f"""
        La causa más frecuente fue el código ICD-10
        **{causa_max}** con
        **{total_causa:,} casos**.
        """
    )

    # CONCLUSIÓN GENERAL
   

    st.success(
        """
        El análisis de mortalidad evidencia
        variaciones según territorio, sexo, edad
        y causa de muerte.
        """
    )