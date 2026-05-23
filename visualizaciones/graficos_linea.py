import pandas as pd
import plotly.express as px
import streamlit as st


def grafico_muertes_por_mes(df: pd.DataFrame) -> None:
    """
    Genera un gráfico de línea con la cantidad de muertes
    registradas por mes.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con datos de mortalidad.

    Retorna
    -------
    None
    """

    # Agrupar por mes
    muertes_mes = (
        df.groupby("MES_TEXTO")
        .size()
        .reset_index(name="TOTAL")
    )

    # Orden de meses
    orden_meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # Convertir a categoría ordenada
    muertes_mes["MES_TEXTO"] = pd.Categorical(
        muertes_mes["MES_TEXTO"],
        categories=orden_meses,
        ordered=True
    )

    # Ordenar datos
    muertes_mes = muertes_mes.sort_values("MES_TEXTO")

    # Crear gráfico
    fig = px.line(
        muertes_mes,
        x="MES_TEXTO",
        y="TOTAL",
        markers=True,
        title="Muertes registradas por mes"
    )

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)