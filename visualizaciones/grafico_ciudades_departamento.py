import pandas as pd
import plotly.express as px
import streamlit as st


def grafico_ciudades_departamento(df: pd.DataFrame) -> None:
    """
    Muestra muertes por ciudad o municipio.
    """

    # Agrupar datos
    data = (
        df.groupby("CIUDAD_TEXTO")
        .size()
        .reset_index(name="TOTAL_MUERTES")
        .sort_values("TOTAL_MUERTES", ascending=False)
    )

    # Crear gráfico
    fig = px.bar(
        data,
        x="CIUDAD_TEXTO",
        y="TOTAL_MUERTES",
        text_auto=True,
        title="Distribución de muertes por ciudad / municipio",
        labels={
            "CIUDAD_TEXTO": "Ciudad",
            "TOTAL_MUERTES": "Muertes"
        }
    )

    
    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        font=dict(size=13)
    )

    fig.update_traces(textposition="outside")

    # Mostrar
    st.plotly_chart(fig, use_container_width=True)