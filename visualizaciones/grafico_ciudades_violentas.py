import pandas as pd
import plotly.express as px
import streamlit as st


def grafico_ciudades_violentas(df: pd.DataFrame) -> None:
    """
    Muestra top 5 ciudades con homicidios.
    """

    # Filtrar homicidios
    homicidios = df[df["MANERA_MUERTE_TEXTO"] == "Homicidio"].copy()

    # Limpiar datos
    homicidios = homicidios[
        homicidios["CIUDAD_TEXTO"].notna()
    ]

    homicidios = homicidios[
        ~homicidios["CIUDAD_TEXTO"].isin(
            ["Sin información", "Ciudad desconocida", "Municipio desconocido"]
        )
    ]

    # Agrupar
    top = (
        homicidios.groupby("CIUDAD_TEXTO")
        .size()
        .reset_index(name="TOTAL_HOMICIDIOS")
        .sort_values("TOTAL_HOMICIDIOS", ascending=False)
        .head(5)
    )

    # Validación
    if top.empty:
        st.warning("Sin datos de homicidios.")
        return

    # Gráfico
    fig = px.bar(
        top,
        x="CIUDAD_TEXTO",
        y="TOTAL_HOMICIDIOS",
        text_auto=True,
        title="Top 5 ciudades con más homicidios",
        labels={
            "CIUDAD_TEXTO": "Ciudad",
            "TOTAL_HOMICIDIOS": "Homicidios"
        }
    )

    # Estilo
    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        font=dict(size=13)
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)