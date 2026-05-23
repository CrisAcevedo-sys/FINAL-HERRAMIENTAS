"""
Diccionario ICD-10 utilizado para traducir códigos
de causas de muerte a descripciones médicas entendibles.

ICD-10 significa:
International Classification of Diseases 10th Revision.

En español:
Clasificación Internacional de Enfermedades
Décima Revisión.

Este sistema fue desarrollado por la OMS
(Organización Mundial de la Salud)
y se utiliza internacionalmente para:

- registrar enfermedades,
- clasificar causas de muerte,
- identificar lesiones,
- analizar estadísticas de salud pública.

Estructura de los códigos ICD-10
--------------------------------

Cada código posee:
- una letra inicial,
- números,
- y en algunos casos caracteres adicionales.

Ejemplos:
---------
I219 -> Infarto agudo de miocardio
J189 -> Neumonía no especificada
X950 -> Homicidio con arma de fuego

Clasificación general:
----------------------

A-B -> Enfermedades infecciosas
C-D -> Tumores y cáncer
E -> Enfermedades endocrinas
I -> Enfermedades cardiovasculares
J -> Enfermedades respiratorias
V-Y -> Accidentes, homicidios y violencia

Este diccionario permite transformar los códigos
originales del DANE en nombres médicos comprensibles
para facilitar:
- análisis estadístico,
- visualizaciones,
- interpretación de datos.
"""

# Diccionario principal ICD-10
# Formato:
# "CODIGO": "DESCRIPCIÓN MÉDICA"

ICD10_MAP: dict[str, str] = {

    # Enfermedades cardiovasculares
    "I219": "Infarto agudo de miocardio",
    "I10X": "Hipertensión esencial",

    # Diabetes y enfermedades endocrinas
    "E149": "Diabetes mellitus no especificada",

    # Enfermedades respiratorias
    "J189": "Neumonía no especificada",
    "J449": "EPOC no especificada",

    # Tumores y cáncer
    "C349": "Tumor maligno de pulmón",
    "C509": "Cáncer de mama",

    # Enfermedades infecciosas
    "N390": "Infección urinaria",
    "A419": "Sepsis no especificada",

    # Violencia y homicidios
    #
    # Los códigos X93-X95 corresponden a agresiones
    # con armas de fuego según clasificación OMS.
    "X930": "Agresión con arma corta",
    "X940": "Agresión con rifle o escopeta",
    "X950": "Homicidio con arma de fuego",
    "X959": "Homicidio por arma de fuego no especificado",

    # Accidentes y transporte
    "V899": "Accidente de transporte no especificado",
    "V499": "Accidente automovilístico",

    # Suicidios y autolesiones
    "X700": "Lesión autoinfligida por ahorcamiento",

    # Otras causas frecuentes
    "R99X": "Causa mal definida",

    # COVID-19
    #
    # Código implementado por la OMS
    # durante la pandemia.
    "U071": "COVID-19 identificado",
}