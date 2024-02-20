from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

"""
When we call PokemonRepository#all
We get a list of Pokemon objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/pokemon_store.sql")
    repository = PokemonRepository(db_connection) 

    pokemons = repository.all()

    # Assert on the results
    assert pokemons == [
        Pokemon(1, "Pikachu", "electric"),
        Pokemon(2, "Raichu", "electric"),
        Pokemon(3, "Charmander", "fire"),
        Pokemon(4, "Bulbasaur", "earth"),
        Pokemon(5, "Mewtwo", "psychic"),
    ]

"""
When we call PokemonRepository#find
We get a single Pokemon object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/pokemon_store.sql")
    repository = PokemonRepository(db_connection)

    pokemon = repository.find(3)
    assert pokemon == Pokemon(3, "Charmander", "fire")

"""
When we call PokemonRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/pokemon_store.sql")
    repository = PokemonRepository(db_connection)

    created_pokemon = repository.create(Pokemon(None, "Venusaur", "earth"))
    assert created_pokemon == Pokemon(6, "Venusaur", "earth")

    result = repository.all()
    assert result == [
        Pokemon(1, "Pikachu", "electric"),
        Pokemon(2, "Raichu", "electric"),
        Pokemon(3, "Charmander", "fire"),
        Pokemon(4, "Bulbasaur", "earth"),
        Pokemon(5, "Mewtwo", "psychic"),
        Pokemon(6, "Venusaur", "earth")
    ]

"""
When we call PokemonRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/pokemon_store.sql")
    repository = PokemonRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Pokemon(1, "Pikachu", "electric"),
        Pokemon(2, "Raichu", "electric"),
        Pokemon(4, "Bulbasaur", "earth"),
        Pokemon(5, "Mewtwo", "psychic")
    ]
