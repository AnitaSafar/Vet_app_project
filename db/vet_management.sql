DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    specialties VARCHAR(255),
    reg_number INT
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type VARCHAR(255),
    owner VARCHAR(255),
    notes VARCHAR(255),
    vet_id INT REFERENCES vets(id)
);