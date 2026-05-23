import streamlit as st
import plotly.express as px
import pandas as pd


def grafico_barras_apiladas(df: pd.DataFrame) -> None:
    """
    Genera un gráfico de barras apiladas que compara la
    cantidad de muertes por sexo en cada departamento.

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
    datos = datos[datos["DEPARTAMENTO_TEXTO"].notna()]
    datos = datos[datos["SEXO_TEXTO"].notna()]

    # Agrupar por departamento y sexo
    sexo_departamento = (
        datos.groupby(["DEPARTAMENTO_TEXTO", "SEXO_TEXTO"])
        .size()
        .reset_index(name="TOTAL_MUERTES")
    )

    # Orden de departamentos por total de muertes
    orden_departamentos = (
        sexo_departamento.groupby("DEPARTAMENTO_TEXTO")["TOTAL_MUERTES"]
        .sum()
        .sort_values(ascending=False)
        .index
    )

    # Crear gráfico
    fig = px.bar(
        sexo_departamento,
        x="DEPARTAMENTO_TEXTO",
        y="TOTAL_MUERTES",
        color="SEXO_TEXTO",
        barmode="stack",
        category_orders={
            "DEPARTAMENTO_TEXTO": orden_departamentos
        },
        title="Comparación de muertes por sexo en cada departamento",
        labels={
            "DEPARTAMENTO_TEXTO": "Departamento",
            "TOTAL_MUERTES": "Total de muertes",
            "SEXO_TEXTO": "Sexo"
        }
    )

    # Ajustes de diseño
    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        xaxis_tickangle=-45,
        height=700
    )

    # Hover personalizado
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>"
                      "Sexo: %{fullData.name}<br>"
                      "Muertes: %{y:,}<extra></extra>"
    )

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

    # Departamento con mayor mortalidad
    depto_max: str = (
        sexo_departamento.groupby("DEPARTAMENTO_TEXTO")["TOTAL_MUERTES"]
        .sum()
        .idxmax()
    )

    total_max: int = int(
        sexo_departamento.groupby("DEPARTAMENTO_TEXTO")["TOTAL_MUERTES"]
        .sum()
        .max()
    )

    st.info(
        f"El departamento con mayor cantidad de muertes registradas fue "
        f"**{depto_max}** con **{total_max:,} casos**."
    )