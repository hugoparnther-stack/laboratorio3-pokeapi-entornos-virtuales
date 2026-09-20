"""Manejo de la base de datos local (SQLite).

El archivo .db se crea solo la primera vez y NO se sube a GitHub
(está excluido en el .gitignore).
"""

import sqlite3
from datetime import datetime

from src.config import DB_PATH


def conectar(ruta=None):
    """Abre la conexión a la base de datos (y crea la carpeta /data si falta)."""
    ruta = ruta or DB_PATH
    ruta.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(ruta)


def crear_tabla(conexion):
    """Crea la tabla pokemon si todavía no existe."""
    conexion.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            altura INTEGER,
            peso INTEGER,
            experiencia_base INTEGER,
            tipos TEXT,
            habilidades TEXT,
            fecha_consulta TEXT
        )
        """
    )
    conexion.commit()


def guardar_pokemon(conexion, pokemon):
    """Guarda un Pokémon. Si ya existe (mismo id), lo actualiza."""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conexion.execute(
        """
        INSERT OR REPLACE INTO pokemon
            (id, nombre, altura, peso, experiencia_base, tipos, habilidades, fecha_consulta)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon["id"],
            pokemon["nombre"],
            pokemon["altura"],
            pokemon["peso"],
            pokemon["experiencia_base"],
            pokemon["tipos"],
            pokemon["habilidades"],
            fecha,
        ),
    )
    conexion.commit()


def listar_pokemon(conexion):
    """Devuelve todos los Pokémon guardados, ordenados por id."""
    cursor = conexion.execute(
        "SELECT id, nombre, altura, peso, experiencia_base, tipos, habilidades "
        "FROM pokemon ORDER BY id"
    )
    return cursor.fetchall()
