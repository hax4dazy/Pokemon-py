from peewee import *
from dbClasses import *

db = SqliteDatabase("database.db", pragmas={"foreign_keys": 1})

class setupDB():
    #cursed code
    db.create_tables([PokemonData], safe=True)
    PokemonData.get_or_create(pokemonType="normal", SE="", NVE="rock, steel", NE="ghost")
    PokemonData.get_or_create(pokemonType="fire", SE="grass, ice, bug, steel", NVE="fire, water, rock, dragon", NE="")
    PokemonData.get_or_create(pokemonType="water", SE="fire, ground, rock", NVE="water, grass, dragon", NE="")
    PokemonData.get_or_create(pokemonType="electric", SE="water, flying", NVE="electric, grass, dragon", NE="ground")
    PokemonData.get_or_create(pokemonType="grass", SE="water, ground, rock", NVE="fire, grass, poison, flying, bug, dragon, steel", NE="")
    PokemonData.get_or_create(pokemonType="ice", SE="grass, ground, flying, dragon", NVE="fire, water, ice, steel", NE="")
    PokemonData.get_or_create(pokemonType="fighting", SE="normal, ice, rock, dark, steel", NVE="poison, flying, psychic, bug, fairy", NE="ghost")
    PokemonData.get_or_create(pokemonType="poison", SE="grass, fairy", NVE="poison, ground, rock, ghost", NE="")
    PokemonData.get_or_create(pokemonType="ground", SE="fire, electric, poison, rock, steel", NVE="grass, bug", NE="flying")
    PokemonData.get_or_create(pokemonType="flying", SE="grass, fighting, bug", NVE="electric, rock, steel", NE="")
    PokemonData.get_or_create(pokemonType="psychic", SE="fighting, poison", NVE="psychic, steel", NE="dark")
    PokemonData.get_or_create(pokemonType="bug", SE="grass, psychic, dark", NVE="fire, fighting, poison, flying, ghost, steel, fairy", NE="")
    PokemonData.get_or_create(pokemonType="rock", SE="fire, ice, flying, bug", NVE="fighting, ground, steel", NE="")
    PokemonData.get_or_create(pokemonType="ghost", SE="psychic, ghost", NVE="dark", NE="normal")
    PokemonData.get_or_create(pokemonType="dragon", SE="dragon", NVE="steel", NE="fairy")
    PokemonData.get_or_create(pokemonType="dark", SE="psychic, ghost", NVE="fighting, dark, fairy", NE="psychic")
    PokemonData.get_or_create(pokemonType="steel", SE="ice, rock, fairy", NVE="fire, water, electric, steel", NE="")
    PokemonData.get_or_create(pokemonType="fairy", SE="fighting, dragon, dark", NVE="fire, poison, steel", NE="")
