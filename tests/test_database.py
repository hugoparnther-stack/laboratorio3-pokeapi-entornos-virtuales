"""Pruebas de la base de datos (usan una base temporal, no tocan data/pokedex.db)."""

from src.database import conectar, crear_tabla, guardar_pokemon, listar_pokemon

PIKACHU = {
    "id": 25,
    "nombre": "pikachu",
    "altura": 4,
    "peso": 60,
    "experiencia_base": 112,
    "tipos": "electric",
    "habilidades": "static, lightning-rod",
}


def test_guardar_y_listar(tmp_path):
    conexion = conectar(tmp_path / "prueba.db")
    crear_tabla(conexion)

    guardar_pokemon(conexion, PIKACHU)
    filas = listar_pokemon(conexion)

    assert len(filas) == 1
    assert filas[0][1] == "pikachu"
    conexion.close()


def test_guardar_dos_veces_no_duplica(tmp_path):
    conexion = conectar(tmp_path / "prueba.db")
    crear_tabla(conexion)

    guardar_pokemon(conexion, PIKACHU)
    guardar_pokemon(conexion, PIKACHU)

    assert len(listar_pokemon(conexion)) == 1
    conexion.close()
