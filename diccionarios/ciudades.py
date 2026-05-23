"""
Diccionario de municipios y ciudades de Colombia
utilizando códigos DIVIPOLA oficiales del DANE.

DIVIPOLA significa:
División Político-Administrativa de Colombia.

Este sistema es utilizado por el DANE para identificar
de forma única:
- departamentos,
- municipios,
- corregimientos,
- centros poblados.

Estructura del código DIVIPOLA:
--------------------------------

Los códigos están compuestos por:

2 dígitos -> departamento
3 dígitos -> municipio

Ejemplos:
---------
05001 -> Medellín
11 001 -> Bogotá D.C.
76 001 -> Cali

Esto permite identificar municipios incluso si existen
nombres repetidos en diferentes departamentos.

IMPORTANTE
-----------
Las claves del diccionario deben almacenarse como str
y NO como int.

Esto se hace para conservar los ceros a la izquierda.

Ejemplo:
--------
Correcto:
"05001"

Incorrecto:
5001

Si se utiliza int, Python eliminaría el cero inicial,
rompiendo la correspondencia con el código oficial DANE.
"""

# Diccionario principal de ciudades y municipios
# Formato:
# "DIVIPOLA": "Nombre del municipio"

CIUDADES_MAP: dict[str, str] = {

    # Antioquia
    "05001": "Medellín",
    "05002": "Abejorral",
    "05004": "Abriaquí",
    "05021": "Alejandría",
    "05030": "Amagá",
    "05031": "Amalfi",
    "05034": "Andes",
    "05036": "Angelópolis",
    "05038": "Angostura",
    "05040": "Anorí",
    "05042": "Santa Fe de Antioquia",
    "05044": "Anzá",
    "05045": "Apartadó",
    "05051": "Arboletes",
    "05055": "Argelia",
    "05059": "Armenia",
    "05079": "Barbosa",
    "05086": "Belmira",
    "05088": "Bello",
    "05091": "Betania",
    "05093": "Betulia",

    # Bogotá
    "11001": "Bogotá D.C.",

    # Atlántico
    "08001": "Barranquilla",
    "08758": "Soledad",

    # Valle del Cauca
    "76001": "Cali",
    "76109": "Buenaventura",
    "76834": "Tuluá",

    # Santander
    "68001": "Bucaramanga",
    "68081": "Barrancabermeja",

    # Bolívar
    "13001": "Cartagena",

    # Caldas
    "17001": "Manizales",

    # Risaralda
    "66001": "Pereira",

    # Quindío
    "63001": "Armenia",

    # Tolima
    "73001": "Ibagué",

    # Meta
    "50001": "Villavicencio",

    # Norte de Santander
    "54001": "Cúcuta",

    # Nariño
    "52001": "Pasto",

    # Magdalena
    "47001": "Santa Marta",

    # Huila
    "41001": "Neiva",

    # Córdoba
    "23001": "Montería",

    # Cesar
    "20001": "Valledupar",

    # Sucre
    "70001": "Sincelejo",

    # Casanare
    "85001": "Yopal",
}