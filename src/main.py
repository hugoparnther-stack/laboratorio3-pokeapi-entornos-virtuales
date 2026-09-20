"""Programa principal: consulta la PokéAPI y guarda los resultados en SQLite.

Uso (desde la carpeta raíz del proyecto, con el venv activado):

    python -m src.main pikachu bulbasaur charizard
    python -m src.main --listar
"""

import argparse

import requests

from src.api_client import PokemonNoEncontrado, obtener_pokemon
from src.database import conectar, crear_tabla, guardar_pokemon, listar_pokemon


def buscar_y_guardar(nombres):
    """Consulta cada Pokémon en la API y lo guarda en la base de datos."""
    conexion = conectar()
    crear_tabla(conexion)

    for nombre in nombres:
        try:
            pokemon = obtener_pokemon(nombre)
        except PokemonNoEncontrado as error:
            print(f"[!] {error}")
            continue
        except requests.exceptions.RequestException as error:
            print(f"[!] Error de conexión con la API: {error}")
            continue

        guardar_pokemon(conexion, pokemon)
        print(f"[OK] {pokemon['nombre'].capitalize()} (#{pokemon['id']}) guardado")

    conexion.close()


def mostrar_guardados():
    """Muestra en pantalla todos los Pokémon que hay en la base de datos."""
    conexion = conectar()
    crear_tabla(conexion)
    filas = listar_pokemon(conexion)
    conexion.close()

    if not filas:
        print("Todavía no hay Pokémon guardados. Prueba: python -m src.main pikachu")
        return

    print(f"{'ID':<5}{'NOMBRE':<14}{'TIPOS':<20}HABILIDADES")
    print("-" * 60)
    for id_, nombre, _altura, _peso, _exp, tipos, habilidades in filas:
        print(f"{id_:<5}{nombre:<14}{tipos:<20}{habilidades}")


def main():
    parser = argparse.ArgumentParser(description="Consulta Pokémon en la PokéAPI")
    parser.add_argument("nombres", nargs="*", help="nombres de Pokémon a consultar")
    parser.add_argument(
        "--listar", action="store_true", help="muestra los Pokémon guardados"
    )
    args = parser.parse_args()

    if args.listar:
        mostrar_guardados()
    elif args.nombres:
        buscar_y_guardar(args.nombres)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
