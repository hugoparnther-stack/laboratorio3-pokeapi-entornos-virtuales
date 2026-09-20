"""Cliente para consultar la PokéAPI con requests."""

import requests

from src.config import API_BASE_URL, API_TIMEOUT


class PokemonNoEncontrado(Exception):
    """Se lanza cuando la API responde 404 (el Pokémon no existe)."""


def obtener_pokemon(nombre):
    """Consulta un Pokémon por nombre y devuelve sus datos principales.

    Hace el mismo GET que hicimos en Postman:
    https://pokeapi.co/api/v2/pokemon/<nombre>
    """
    url = f"{API_BASE_URL}/pokemon/{nombre.lower().strip()}"
    respuesta = requests.get(url, timeout=API_TIMEOUT)

    if respuesta.status_code == 404:
        raise PokemonNoEncontrado(f"No existe el Pokémon '{nombre}'")

    # Si hubo otro error (500, 403, etc.) esto lanza una excepción
    respuesta.raise_for_status()

    datos = respuesta.json()

    # Nos quedamos solo con lo que vamos a guardar
    return {
        "id": datos["id"],
        "nombre": datos["name"],
        "altura": datos["height"],
        "peso": datos["weight"],
        # Algunas formas especiales de Pokémon vienen con base_experience = null
        "experiencia_base": datos.get("base_experience"),
        "tipos": ", ".join(t["type"]["name"] for t in datos["types"]),
        "habilidades": ", ".join(a["ability"]["name"] for a in datos["abilities"]),
    }
