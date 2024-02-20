-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS pokemons;
DROP SEQUENCE IF EXISTS pokemons_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS pokemons_id_seq;
CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO pokemons (name, type) VALUES ('Pikachu', 'electric');
INSERT INTO pokemons (name, type) VALUES ('Raichu', 'electric');
INSERT INTO pokemons (name, type) VALUES ('Charmander', 'fire');
INSERT INTO pokemons (name, type) VALUES ('Bulbasaur', 'earth');
INSERT INTO pokemons (name, type) VALUES ('Mewtwo', 'psychic');
