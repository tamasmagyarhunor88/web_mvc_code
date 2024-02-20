from lib.pokemon import Pokemon

"""
Pokemon constructs with an id, name and type
"""
def test_pokemon_constructs():
    pokemon = Pokemon(1, "Pikachu", "electric")
    assert pokemon.id == 1
    assert pokemon.name == "Pikachu"
    assert pokemon.type == "electric"

"""
We can format pokemons to strings nicely
"""
def test_pokemons_format_nicely():
    pokemon = Pokemon(1, "Pikachu", "electric")
    assert str(pokemon) == "Pokemon(1, Pikachu, electric)"

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    pokemon = Pokemon(1, "Pikachu", "electric")
    pokemon2 = Pokemon(1, "Pikachu", "electric")
    assert pokemon == pokemon2
