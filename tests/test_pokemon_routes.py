from playwright.sync_api import Page, expect

"""
We can list out all the pokemons
"""
def test_get_pokemons(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")

    page.goto(f"http://{test_web_address}/pokemons")

    list_items = page.locator("li")

    expect(list_items).to_have_text([
        "Pikachu - electric",
        "Raichu - electric",
        "Charmander - fire",
        "Bulbasaur - earth",
        "Mewtwo - psychic",
    ])

"""
We can retrieve a single pokemon
"""
def test_get_pokemon(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")

    page.goto(f"http://{test_web_address}/pokemons")

    page.click("text=Pikachu")

    name_element = page.locator(".t-name")
    expect(name_element).to_have_text("name: Pikachu")

    type_element = page.locator(".t-type")
    expect(type_element).to_have_text("type: electric")

"""
When we create a new pokemon
We see it in the pokemons index
"""
def test_create_pokemon(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")
    page.goto(f"http://{test_web_address}/pokemons")

    page.click("text=Add a new pokemon")

    page.fill("input[name='name']", "Venusaur")

    page.fill("input[name='type']", "earth")

    page.click("text=Create Pokemon")

    name_element = page.locator(".t-name")
    expect(name_element).to_have_text("name: Venusaur")

    type_element = page.locator(".t-type")
    expect(type_element).to_have_text("type: earth")

"""
If we create a new pokemon without a name or type
We see an error message
"""
def test_create_pokemon_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")
    page.goto(f"http://{test_web_address}/pokemons")
    page.click("text=Add a new pokemon")
    page.click("text=Create Pokemon")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Type can't be blank")

"""
When we delete a pokemon
We no longer see it in the pokemons index
"""
def test_delete_pokemon(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")
    page.goto(f"http://{test_web_address}/pokemons")
    page.click("text=Raichu")
    page.click("text=Delete Pokemon")
    list_items = page.locator("li")
    expect(list_items).to_have_text([
        "Pikachu - electric",
        "Charmander - fire",
        "Bulbasaur - earth",
        "Mewtwo - psychic",
    ])