DROP TABLE kegs
DROP TABLE beers
DROP TABLE breweries

CREATE TABLE breweries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)

CREATE TABLE beers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    abv FLOAT,
    brewery_id INT NOT NULL REFERENCES breweries(id)
)

CREATE TABLE kegs (
    id SERIAL PRIMARY KEY,
    beer_id INT NOT NULL REFERENCES beers(id),
    fill_level INT,
    capacity INT NOT NULL
)