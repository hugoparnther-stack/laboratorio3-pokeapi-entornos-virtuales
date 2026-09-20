"""Configuración del proyecto.

Lee las variables del archivo .env (si existe) y define valores por defecto,
así la app funciona aunque el .env no exista.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Carpeta raíz del proyecto (la que contiene /src, /data y /tests)
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga las variables del archivo .env que está en la raíz del proyecto
load_dotenv(BASE_DIR / ".env")

# URL base de la API
API_BASE_URL = os.getenv("API_BASE_URL", "https://pokeapi.co/api/v2")

# Segundos que esperamos la respuesta de la API antes de rendirnos
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))

# Ruta de la base de datos local (relativa a la raíz del proyecto)
DB_PATH = BASE_DIR / os.getenv("DB_PATH", "data/pokedex.db")
