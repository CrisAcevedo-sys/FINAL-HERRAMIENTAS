import streamlit as st
import plotly.express as px
import pandas as pd


def grafico_grupo_edad(df: pd.DataFrame) -> None:
    """
    Genera un gráfico de barras con la distribución de muertes
    por grupo de edad.

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

    # Eliminar valores nulos
    datos = datos[datos["GRUPO_EDAD_TEXTO"].notna()]

    # Orden de categorías
    orden_edades = [
        "Mortalidad neonatal",
        "Mortalidad infantil",
        "Primera infancia",
        "Niñez",
        "Adolescencia",
        "Juventud",
        "Adultez temprana",
        "Adultez intermedia",
        "Vejez",
        "Longevidad / Centenarios",
        "Edad desconocida"
    ]

    # Agrupar por grupo de edad
    grupo_edad = (
        datos.groupby("GRUPO_EDAD_TEXTO")
        .size()
        .reset_index(name="TOTAL_MUERTES")
    )

    # Convertir a categoría ordenada
    grupo_edad["GRUPO_EDAD_TEXTO"] = (
        grupo_edad["GRUPO_EDAD_TEXTO"].astype("category")
    )

    grupo_edad["GRUPO_EDAD_TEXTO"] = (
        grupo_edad["GRUPO_EDAD_TEXTO"].cat.set_categories(
            orden_edades,
            ordered=True
        )
    )

    # Ordenar categorías
    grupo_edad = grupo_edad.sort_values("GRUPO_EDAD_TEXTO")

    # Crear gráfico
    fig = px.bar(
        grupo_edad,
        x="GRUPO_EDAD_TEXTO",
        y="TOTAL_MUERTES",
        text_auto=True,
        title="Distribución de muertes por grupo de edad",
        labels={
            "GRUPO_EDAD_TEXTO": "Grupo de edad",
            "TOTAL_MUERTES": "Total de muertes"
        }
    )

    # Estilo del gráfico
    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        xaxis_tickangle=-20,
        height=600
    )

    # Hover personalizado
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>"
                      "Muertes: %{y:,}<extra></extra>"
    )

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

    # Grupo con mayor mortalidad
    grupo_max = grupo_edad.loc[
        grupo_edad["TOTAL_MUERTES"].idxmax()
    ]

    st.info(
        f"El grupo con mayor cantidad de muertes fue "
        f"**{grupo_max['GRUPO_EDAD_TEXTO']}** con "
        f"**{grupo_max['TOTAL_MUERTES']:,} casos**."
    )