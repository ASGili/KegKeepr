DROP TABLE kegs;
DROP TABLE beers;
DROP TABLE breweries;

CREATE TABLE breweries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE beers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    abv FLOAT,
    brewery_id INT NOT NULL REFERENCES breweries(id) ON DELETE CASCADE
);

CREATE TABLE kegs (
    id SERIAL PRIMARY KEY,
    fill_level INT,
    capacity INT NOT NULL,
    cost INT,
    price INT,
    beer_id INT NOT NULL REFERENCES beers(id) ON DELETE CASCADE
);