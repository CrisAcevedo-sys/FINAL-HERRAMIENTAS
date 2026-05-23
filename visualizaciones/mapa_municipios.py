import json
import pandas as pd
import plotly.express as px
import streamlit as st


def mapa_municipios(df: pd.DataFrame) -> None:
    """
    Genera un mapa coroplético a nivel de municipios
    con la distribución de muertes en Colombia.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con datos de mortalidad.

    Retorna
    -------
    None
    """

    # Cargar GeoJSON
    with open(
        "mapas/municipios_colombia.geojson",
        encoding="utf-8"
    ) as f:
        geojson = json.load(f)

    # Copia del DataFrame
    datos = df.copy()

    # Formatear código DIVIPOLA
    datos["DIVIPOLA"] = (
        datos["DIVIPOLA"]
        .astype(str)
        .str.zfill(5)
    )

    # Agrupar por municipio
    municipios = (
        datos.groupby(
            ["DIVIPOLA", "CIUDAD_TEXTO", "DEPARTAMENTO_TEXTO"]
        )
        .size()
        .reset_index(name="TOTAL_MUERTES")
    )

    # Crear mapa
    fig = px.choropleth_mapbox(
        municipios,
        geojson=geojson,
        locations="DIVIPOLA",
        featureidkey="properties.MPIO_CCNCT",
        color="TOTAL_MUERTES",
        hover_name="CIUDAD_TEXTO",
        hover_data={
            "DEPARTAMENTO_TEXTO": True,
            "TOTAL_MUERTES": True,
            "DIVIPOLA": False
        },
        color_continuous_scale="Reds",
        mapbox_style="carto-positron",
        zoom=4.3,
        center={"lat": 4.5709, "lon": -74.2973},
        opacity=0.75,
        title="Distribución de muertes por municipios en Colombia"
    )

    # Ajustes de diseño
    fig.update_layout(
        margin=dict(r=0, t=50, l=0, b=0),
        height=750
    )

    # Hover personalizado
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>"
                      "Muertes: %{z:,}<br>"
                      "<extra></extra>"
    )

    # Mostrar mapa
    st.plotly_chart(fig, use_container_width=True)