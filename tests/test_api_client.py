"""Pruebas del cliente de la API.

Usamos una respuesta falsa para no depender de internet al correr los tests.
"""

import pytest

from src import api_client


class RespuestaFalsa:
    """Imita lo mínimo de una respuesta de requests."""

    def __init__(self, status_code, datos=None):
        self.status_code = status_code
        self._datos = datos

    def json(self):
        return self._datos

    def raise_for_status(self):
        pass


def test_obtener_pokemon_devuelve_datos(monkeypatch):
    datos_api = {
        "id": 25,
        "name": "pikachu",
        "height": 4,
        "weight": 60,
        "base_experience": 112,
        "types": [{"type": {"name": "electric"}}],
        "abilities": [{"ability": {"name": "static"}}],
    }
    monkeypatch.setattr(
        api_client.requests, "get", lambda url, timeout: RespuestaFalsa(200, datos_api)
    )

    resultado = api_client.obtener_pokemon("Pikachu")

    assert resultado["id"] == 25
    assert resultado["nombre"] == "pikachu"
    assert resultado["tipos"] == "electric"
    assert resultado["habilidades"] == "static"


def test_experiencia_base_nula_no_rompe(monkeypatch):
    datos_api = {
        "id": 10001,
        "name": "forma-especial",
        "height": 5,
        "weight": 50,
        "base_experience": None,
        "types": [{"type": {"name": "normal"}}],
        "abilities": [{"ability": {"name": "run-away"}}],
    }
    monkeypatch.setattr(
        api_client.requests, "get", lambda url, timeout: RespuestaFalsa(200, datos_api)
    )

    assert api_client.obtener_pokemon("forma-especial")["experiencia_base"] is None


def test_pokemon_inexistente_lanza_error(monkeypatch):
    monkeypatch.setattr(
        api_client.requests, "get", lambda url, timeout: RespuestaFalsa(404)
    )

    with pytest.raises(api_client.PokemonNoEncontrado):
        api_client.obtener_pokemon("noexiste")
