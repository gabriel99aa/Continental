DB = [
    {
        "country": "COLOMBIA",
        "PIB_pre": 3.2,
        "PIB_in": -7,
        "PIB_pos": 10.7,
        "continent": "AMERICA",
    },
    {
        "country": "BRASIL",
        "PIB_pre": 1.2,
        "PIB_in": -3.9,
        "PIB_pos": 4.6,
        "continent": "AMERICA",
    },
    {
        "country": "FRANCIA",
        "PIB_pre": 1.9,
        "PIB_in": -7.8,
        "PIB_pos": 6.8,
        "continent": "EUROPA",
    },
    {
        "country": "PORTUGAL",
        "PIB_pre": 2.7,
        "PIB_in": -8.3,
        "PIB_pos": 5.5,
        "continent": "EUROPA",
    },
    {
        "country": "CHINA",
        "PIB_pre": 6,
        "PIB_in": 2.2,
        "PIB_pos": 8.1,
        "continent": "ASIA",
    },
    {
        "country": "RUSIA",
        "PIB_pre": 2.2,
        "PIB_in": -2.7,
        "PIB_pos": 4.7,
        "continent": "ASIA",
    },
    {
        "country": "MARRUECOS",
        "PIB_pre": 2.9,
        "PIB_in": -7.2,
        "PIB_pos": 7.9,
        "continent": "AFRICA",
    },
    {
        "country": "SUDAFRICA",
        "PIB_pre": 0.3,
        "PIB_in": -6.3,
        "PIB_pos": 4.9,
        "continent": "AFRICA",
    },
    {
        "country": "AUSTRALIA",
        "PIB_pre": 2.2,
        "PIB_in": -0.1,
        "PIB_pos": 2.2,
        "continent": "OSEANIAS",
    },
    {
        "country": "FILIPINAS",
        "PIB_pre": 6.1,
        "PIB_in": -9.5,
        "PIB_pos": 5.7,
        "continent": "OSEANIAS",
    }
]

"""
La anterior base de datos recopila la tasa de crecimiento anual antes,
durante y despues de la pandemia (2019, 2020, 2021), utilizando estos
datos concluya por medio de un programa:
    1. Cual fue el país más afectado durante la pandemia?
    2. Cual fue el que tuvo la mejor recupeción post pandemia?
        nota: para calcular este dato no solo se debe tener en
            cuenta el PIB_pos (2021). debe calcular con respecto 
            al año 2019
    3. Que continente fue el más afectado por la pandemia?
    4. Que continente registró mayor crecimiento en el año 2019
"""

print("tu base de datos es: ")
print("_" * 70)
for obj in DB:
    print(obj.keys())
    break
print("_" * 70)
for obj in DB:
    print(obj.values())
    print("_" * 70)

referencia = 0
masAfectado = {}
for obj in DB:
    if obj.get("PIB_in") < referencia:
        masAfectado = obj
        referencia = obj.get("PIB_in")

referencia2 = 0
mejorRecuperado = {}
for obj in DB:
    ecuacion = (obj.get("PIB_pre") + obj.get("PIB_in") +
                obj.get("PIB_pos"))-obj.get("PIB_pre")
    if ecuacion > referencia2:
        mejorRecuperado = obj
        referencia2 = ecuacion

america = []
europa = []
asia = []
africa = []
oseanias = []

referencia3 = 100
afectacionContinental = ""

for obj in DB:
    if obj.get("continent") == "AMERICA":
        america.append(obj)
    elif obj.get("continent") == "EUROPA":
        europa.append(obj)
    elif obj.get("continent") == "ASIA":
        asia.append(obj)
    elif obj.get("continent") == "AFRICA":
        africa.append(obj)
    else:
        oseanias.append(obj)

decresimientoAmerica = 0
for obj in america:
    decresimientoAmerica += obj.get("PIB_in")
    if decresimientoAmerica < referencia3:
        afectacionContinental = "AMERICA"
        referencia3 = decresimientoAmerica

decresimientoEuropa = 0
for obj in europa:
    decresimientoEuropa += obj.get("PIB_in")
    if decresimientoEuropa < referencia3:
        afectacionContinental = "EUROPA"
        referencia3 = decresimientoEuropa

decresimientoAsia = 0
for obj in asia:
    decresimientoAsia += obj.get("PIB_in")
    if decresimientoAsia < referencia3:
        afectacionContinental = "ASIA"
        referencia3 = decresimientoAsia

decresimientoAfrica = 0
for obj in africa:
    decresimientoAfrica += obj.get("PIB_in")
    if decresimientoAfrica < referencia3:
        afectacionContinental = "AFRICA"
        referencia3 = decresimientoAfrica

decresimientoOseanias = 0
for obj in oseanias:
    decresimientoOseanias += obj.get("PIB_in")
    if decresimientoOseanias < referencia3:
        afectacionContinental = "OSEANIAS"
        referencia3 = decresimientoOseanias

referencia4 = 0
crecimientoContinental = ""

crecimientoAmerica = 0
for obj in america:
    crecimientoAmerica += obj.get("PIB_pre")
    if crecimientoAmerica > referencia4:
        crecimientoContinental = "AMERICA"
        referencia4 = crecimientoAmerica

crecimientoEuropa = 0
for obj in europa:
    crecimientoEuropa += obj.get("PIB_pre")
    if crecimientoEuropa > referencia4:
        crecimientoContinental = "EUROPA"
        referencia4 = crecimientoEuropa

crecimientoAsia = 0
for obj in asia:
    crecimientoAsia += obj.get("PIB_pre")
    if crecimientoAsia > referencia4:
        crecimientoContinental = "ASIA"
        referencia4 = crecimientoAsia

crecimientoAfrica = 0
for obj in africa:
    crecimientoAfrica += obj.get("PIB_pre")
    if crecimientoAfrica > referencia4:
        crecimientoContinental = "AFRICA"
        referencia4 = crecimientoAfrica

crecimientoOseanias = 0
for obj in oseanias:
    crecimientoOseanias += obj.get("PIB_pre")
    if crecimientoOseanias > referencia4:
        crecimientoContinental = "OSEANIAS"
        referencia4 = crecimientoOseanias

print("-" * 70)
nombreAfectado = masAfectado.get("country")
mejor = mejorRecuperado.get("country")
crecimientoMejor = (mejorRecuperado.get(
    "PIB_pre") + mejorRecuperado.get("PIB_in") + mejorRecuperado.get("PIB_pos"))-obj.get("PIB_pre")
print(f"El país más afectado durante la pandemia fue: {nombreAfectado}")
print(f"El que tuvo la mejor recupeción post pandemia fue: {mejor}. ")
print(f"Con un crecimiento del: {crecimientoMejor}%")
print(
    f"El continente más afectado por la pandemia fue: {afectacionContinental}")
print(f"Con un decrecimiento acumulado del: {referencia3}%")
print(
    f"El continente que registró mayor crecimiento en el año 2019: {crecimientoContinental}")
print(f"Con un crecimiento acumulado del: {referencia4}%")
