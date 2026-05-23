import streamlit as st
import plotly.express as px
import pandas as pd


def grafico_menor_mortalidad(df: pd.DataFrame) -> None:
    """
    Genera un gráfico de pastel con las 10 ciudades
    con menor número de muertes registradas.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con datos de mortalidad.

    Retorna
    -------
    None
    """

    # Agrupar por ciudad
    ciudades = (
        df.groupby("CIUDAD_TEXTO")
        .size()
        .reset_index(name="TOTAL_MUERTES")
    )

    # Ordenar de menor a mayor
    ciudades = (
        ciudades.sort_values(
            by="TOTAL_MUERTES",
            ascending=True
        )
        .head(10)
    )

    # Crear gráfico de pastel
    fig = px.pie(
        ciudades,
        names="CIUDAD_TEXTO",
        values="TOTAL_MUERTES",
        title="10 ciudades con menor índice de mortalidad"
    )

    # Estilo
    fig.update_layout(
        template="plotly_dark"
    )

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)