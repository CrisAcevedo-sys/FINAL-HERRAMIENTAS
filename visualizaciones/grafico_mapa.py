import json
from pathlib import Path

import plotly.express as px
import streamlit as st
import pandas as pd


def grafico_mapa(df: pd.DataFrame) -> None:
    """
    Genera un mapa coroplético de Colombia con la distribución
    de muertes por departamento.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con datos de mortalidad.

    Retorna
    -------
    None
    """

    # Ruta GeoJSON
    geojson_path = (
        Path(__file__).resolve().parents[1]
        / "mapas"
        / "colombia_departamentos.geojson"
    )

    # Cargar GeoJSON
    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson_colombia = json.load(f)

    # Agrupar muertes por departamento
    muertes = (
        df.groupby(["DEPARTAMENTO", "DEPARTAMENTO_TEXTO"])
        .size()
        .reset_index(name="TOTAL_MUERTES")
    )

    # Formatear código
    muertes["DEPARTAMENTO"] = (
        muertes["DEPARTAMENTO"]
        .astype(str)
        .str.zfill(2)
    )

    # Crear mapa
    fig = px.choropleth(
        muertes,
        geojson=geojson_colombia,
        locations="DEPARTAMENTO",
        featureidkey="properties.DPTO",
        color="TOTAL_MUERTES",
        hover_name="DEPARTAMENTO_TEXTO",
        hover_data={
            "TOTAL_MUERTES": True,
            "DEPARTAMENTO": False
        },
        color_continuous_scale="Reds",
        projection="mercator",
        title="Distribución de mortalidad por departamento"
    )

 
    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        font=dict(size=13),
        margin=dict(r=0, t=60, l=0, b=0)
    )

    fig.update_coloraxes(colorbar_title="Casos")

    # Mostrar
    st.plotly_chart(fig, use_container_width=True)