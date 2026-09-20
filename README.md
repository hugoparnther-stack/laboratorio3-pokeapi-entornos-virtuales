# Laboratorio 3 — Consultas a la PokéAPI con entornos virtuales

[![Pruebas](https://github.com/hugoparnther-stack/laboratorio3-pokeapi-entornos-virtuales/actions/workflows/tests.yml/badge.svg)](https://github.com/hugoparnther-stack/laboratorio3-pokeapi-entornos-virtuales/actions/workflows/tests.yml)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![Licencia MIT](https://img.shields.io/badge/licencia-MIT-green)

Proyecto del **Laboratorio 3 (Unidad 3: Entornos Virtuales y Gestión de Dependencias)** del
Diplomado en Programación y Desarrollo de Software con Python — Universidad Politécnica Internacional (UPI).

La aplicación consulta la [PokéAPI](https://pokeapi.co) con `requests` (los mismos endpoints que se probaron
en Postman), guarda los resultados en una base de datos SQLite local y permite listarlos desde la consola.
El objetivo del laboratorio es que el proyecto sea **portable**: cualquier persona debe poder clonarlo,
crear su propio entorno virtual e instalarlo solo con `pip install -r requirements.txt`.

## Estructura del proyecto

```
.
├── src/                     # Código de la aplicación
│   ├── config.py            # Lee el .env y define la configuración
│   ├── api_client.py        # Consulta la PokéAPI (requests)
│   ├── database.py          # Guarda y lee datos en SQLite
│   └── main.py              # Programa principal (línea de comandos)
├── data/                    # Aquí se crea la base de datos local (no se versiona)
├── tests/                   # Pruebas con pytest (no necesitan internet)
├── .github/workflows/       # Pruebas automáticas en GitHub Actions
├── .env.example             # Plantilla de variables de entorno
├── .gitignore               # Excluye venv/, __pycache__/, .env y *.db
├── pytest.ini               # Configuración de pytest
├── requirements.txt         # Dependencias de la aplicación (versiones exactas)
├── requirements-dev.txt     # Dependencias de la aplicación + pruebas
└── LICENSE
```

## Requisitos

- Python 3.10 o superior
- Git

## Instalación

**1. Clonar el repositorio**

```bash
git clone https://github.com/hugoparnther-stack/laboratorio3-pokeapi-entornos-virtuales.git
cd laboratorio3-pokeapi-entornos-virtuales
```

**2. Crear y activar el entorno virtual**

```bash
python -m venv venv
```

| Sistema         | Comando de activación      |
| --------------- | -------------------------- |
| Windows (CMD)   | `venv\Scripts\activate`    |
| Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
| macOS / Linux   | `source venv/bin/activate` |

> En PowerShell, si aparece un error de permisos, ejecuta antes:
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

**3. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**4. Crear tu archivo de configuración**

| Sistema         | Comando                     |
| --------------- | --------------------------- |
| Windows         | `copy .env.example .env`    |
| macOS / Linux   | `cp .env.example .env`      |

Los valores por defecto ya funcionan, no necesitas cambiar nada.

## Uso

Consultar uno o varios Pokémon (se guardan en `data/pokedex.db`):

```bash
python -m src.main pikachu bulbasaur charizard
```

Ver los Pokémon guardados:

```bash
python -m src.main --listar
```

Ejemplo de salida:

```
ID   NOMBRE        TIPOS               HABILIDADES
------------------------------------------------------------
1    bulbasaur     grass, poison       overgrow, chlorophyll
6    charizard     fire, flying        blaze, solar-power
25   pikachu       electric            static, lightning-rod
```

Si el nombre no existe, la app avisa y continúa con los demás.

## Pruebas

Las pruebas usan respuestas simuladas y una base de datos temporal, así que no necesitan internet ni tocan tu
`data/pokedex.db`.

```bash
pip install -r requirements-dev.txt
python -m pytest
```

## Variables de entorno

| Variable       | Descripción                      | Valor por defecto           |
| -------------- | -------------------------------- | --------------------------- |
| `API_BASE_URL` | URL base de la API               | `https://pokeapi.co/api/v2` |
| `API_TIMEOUT`  | Segundos de espera por respuesta | `10`                        |
| `DB_PATH`      | Ruta de la base de datos local   | `data/pokedex.db`           |

## Qué no se sube a GitHub

El `.gitignore` excluye `venv/`, `__pycache__/`, `.env` y `*.db`. Por eso quien clone el repositorio crea su
propio entorno virtual y su propio `.env` (a partir de `.env.example`); nunca se comparten entornos ni datos
locales.

## Prueba de portabilidad (clonación cruzada)

Checklist para validar el proyecto en la máquina de un compañero, desde una carpeta limpia:

- [ ] Clonó con `git clone`, sin copiar archivos a mano ni el `venv` de otra persona.
- [ ] Creó su propio `venv` y lo activó.
- [ ] Instaló únicamente con `pip install -r requirements.txt`.
- [ ] Creó su `.env` a partir de `.env.example`.
- [ ] `python -m src.main pikachu` guarda el Pokémon y `python -m src.main --listar` lo muestra.
- [ ] `git status` queda limpio después de usar la app (el `.env` y la `.db` no se versionan).

## Autor

Hugo Parnther — [@hugoparnther-stack](https://github.com/hugoparnther-stack)

Licencia [MIT](LICENSE).
