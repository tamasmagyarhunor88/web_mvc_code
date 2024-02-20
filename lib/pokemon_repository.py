from lib.pokemon import Pokemon

class PokemonRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM pokemons')

        pokemons = []

        for row in rows:
            pokemon = Pokemon(row['id'], row['name'], row['type'])
            pokemons.append(pokemon)
        return pokemons
    
    def find(self, pokemon_id):
        rows = self._connection.execute('SELECT * FROM pokemons WHERE id = %s', [pokemon_id])

        pokemon_dict = rows[0]
        return Pokemon(pokemon_dict['id'], pokemon_dict['name'], pokemon_dict['type'])
    
    def create(self, pokemon):
        rows = self._connection.execute(
            'INSERT INTO pokemons(name, type) VALUES (%s, %s) RETURNING id',
            [pokemon.name, pokemon.type]
        )

        pokemon_created = rows[0]
        pokemon.id = pokemon_created['id']
        return pokemon
    
    def delete(self, pokemon_id):
        self._connection.execute(
            'DELETE FROM pokemons WHERE id = %s', [pokemon_id]
        )
        return None
