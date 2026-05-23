import streamlit as st
import pandas as pd

from componentes.filtros import aplicar_filtros
from componentes.kpis import mostrar_kpis

from visualizaciones.grafico_mapa import grafico_mapa
from visualizaciones.mapa_municipios import mapa_municipios
from visualizaciones.graficos_linea import grafico_muertes_por_mes
from visualizaciones.grafico_ciudades_violentas import grafico_ciudades_violentas
from visualizaciones.grafico_menor_mortalidad import grafico_menor_mortalidad
from visualizaciones.tabla_causas import tabla_principales_causas
from visualizaciones.grafico_ciudades_departamento import grafico_ciudades_departamento
from visualizaciones.graficos_edad import grafico_grupo_edad
from visualizaciones.graficos_barras_apiladas import grafico_barras_apiladas

from interpretaciones.analisis_mortalidad import interpretar_patrones


# CONFIGURACIÓN APP
st.set_page_config(
    page_title="Mortalidad Colombia 2019",
    layout="wide"
)

st.title("Análisis de Mortalidad en Colombia - 2019")

# CARGA DE DATOS
df = pd.read_csv(
    "0.1._Datos_filtrados_y_transformados/0.1._Todos_los_datos_2019_transformado.csv"
)

# FILTROS
df_filtrado = aplicar_filtros(df)

# KPIs
mostrar_kpis(df_filtrado)

# MAPAS

grafico_mapa(df_filtrado)
mapa_municipios(df_filtrado)

# TENDENCIA TEMPORAL

grafico_muertes_por_mes(df_filtrado)

# VIOLENCIA Y CIUDADES

grafico_ciudades_violentas(df_filtrado)
grafico_ciudades_departamento(df_filtrado)
grafico_menor_mortalidad(df_filtrado)

# SALUD Y CAUSAS

tabla_principales_causas(df_filtrado)

# DEMOGRAFÍA

grafico_grupo_edad(df_filtrado)
grafico_barras_apiladas(df_filtrado)

# INTERPRETACIÓN

interpretar_patrones(df_filtrado)