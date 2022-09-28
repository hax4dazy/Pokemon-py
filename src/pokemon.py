import requests
from peewee import *
from dbClasses import *
from dbSetup import *

# Connect to the database
db = SqliteDatabase("database.db", pragmas={"foreign_keys": 1})

API_URL = 'https://pokeapi.co/api/v2/pokemon/'

# Querry the API and return the first type and name of the pokemon
# This not only can do the names of pokemon but also their ID :)
def get_pokemon(pokemon):
    response = requests.get(API_URL + pokemon)
    name = response.json()['name']
    type = response.json()['types']
    re = type[0]['type']['name']
    return re, name

# Returns the type coverage from the database
def getPokemonDataFromDB(type):
    return PokemonData.get(PokemonData.pokemonType == type)

# Main function handles everything from asking the user what their selected pokemon is
# to getting the type of the pokemon and then getting the type coverage from the database
def main():
    ATTK = input("Enter either the name of the attacking Pokémon or its ID: ")
    DEF = input("Enter either the name of the defending Pokémon or its ID: ")
    match DEF:
        case '':
            print("You didn't enter anything!")
        case _:
            DEFQ = get_pokemon(DEF)
            DEFType = getPokemonDataFromDB(DEFQ[0])
            SuperEffective = DEFType.SE
            NotVeryEffective = DEFType.NVE
            NotEffective = DEFType.NE

    match ATTK:
        case '':
            print("You didn't enter anything!")
        case _:
            ATTKQ = get_pokemon(ATTK)

    print(DEFQ[1], DEFType.pokemonType)
    print(ATTKQ[1], ATTKQ[0])

    if ATTKQ[0] in SuperEffective:
        print(ATTKQ[1], "'s attack is very effective against", DEFQ[1])
    elif ATTKQ[0] in NotVeryEffective:
        print(ATTKQ[1], "'s attack is not every effective against", DEFQ[1])
    elif ATTKQ[0] in NotEffective:
        print(ATTKQ[1], "'s attack is not effective against", DEFQ[1])

# Run the program (duh)
main()