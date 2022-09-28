from peewee import *

db = SqliteDatabase("database.db", pragmas={"foreign_keys": 1})

class BaseModel(Model):
    class Meta:
        database = db

class PokemonData(BaseModel):
    pokemonType = CharField(default=None)
    SE = CharField(default=None)
    NVE = CharField(default=False)
    NE = CharField(default=False)