"""Tipos de modulos
- Biblioteca estándar — vienen con Python, no requieren instalación: os, math, datetime, pathlib, etc.
- Externos — instalados con pip desde PyPI: requests, numpy, pandas, etc.
- Propios — archivos .py que escribes tú para tu proyecto.
"""

import datetime
from zoneinfo import ZoneInfo

import requests


def formatear_personaje(datos):
    hora = datetime.datetime.now(ZoneInfo("America/Lima")).strftime("%H:%M:%S")
    return f"[{hora}] {datos['name']} está {datos['status']}"


r = requests.get("https://rickandmortyapi.com/api/character/1")

if r.status_code == 200:
    datos = r.json()
    print(formatear_personaje(datos))
else:
    print("No Encontrado")
